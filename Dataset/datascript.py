import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()
np.random.seed(42)
random.seed(42)

# -----------------------------
# CONFIG
# -----------------------------
NUM_USERS = 10000
START_DATE = datetime(2024, 1, 1)
END_DATE = datetime(2024, 3, 31)

CITIES = ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Pune"]
DEVICE_TYPES = ["Android", "iOS"]
ACQ_CHANNELS = ["Organic", "Instagram Ads", "Google Ads", "Referral"]

USER_TYPES = {
    "power": 0.1,
    "regular": 0.3,
    "occasional": 0.4,
    "one_time": 0.2
}

EVENT_POOL = [
    "browse_category",
    "search",
    "product_view",
    "add_to_cart",
    "remove_from_cart"
]

# -----------------------------
# HELPER FUNCTIONS
# -----------------------------

def peak_hour():
    """Return realistic peak usage hour."""
    r = random.random()
    if r < 0.4:
        return random.randint(7, 10)     # morning peak
    elif r < 0.8:
        return random.randint(18, 23)    # evening peak
    else:
        return random.randint(0, 23)     # random

def weekend_boost(date):
    """More likely to order on weekends."""
    if date.weekday() >= 5:
        return 1.3
    return 1.0

# -----------------------------
# USERS
# -----------------------------
users = []

for user_id in range(1, NUM_USERS + 1):
    signup_date = START_DATE + timedelta(
        days=random.randint(0, (END_DATE - START_DATE).days)
    )
    user_type = np.random.choice(
        list(USER_TYPES.keys()),
        p=list(USER_TYPES.values())
    )

    users.append([
        user_id,
        signup_date,
        random.choice(CITIES),
        random.choice(ACQ_CHANNELS),
        random.choice(DEVICE_TYPES),
        user_type
    ])

users_df = pd.DataFrame(users, columns=[
    "user_id", "signup_date", "city",
    "acquisition_channel", "device_type", "user_type"
])

# -----------------------------
# EVENTS + ORDERS
# -----------------------------

events = []
orders = []

event_id = 1
order_id = 1

for _, user in users_df.iterrows():

    user_id = user["user_id"]
    signup_date = user["signup_date"]
    user_type = user["user_type"]
    city = user["city"]
    device = user["device_type"]

    churned = False
    last_active = signup_date

    # Session count by user type
    if user_type == "power":
        sessions = random.randint(12, 20)
    elif user_type == "regular":
        sessions = random.randint(6, 10)
    elif user_type == "occasional":
        sessions = random.randint(3, 6)
    else:
        sessions = random.randint(1, 2)

    for s in range(sessions):

        if churned:
            break

        session_date = last_active + timedelta(days=random.randint(1, 7))
        if session_date > END_DATE:
            break

        session_start = session_date.replace(
            hour=peak_hour(),
            minute=random.randint(0, 59)
        )

        session_id = f"{user_id}_{s}"
        num_events = random.randint(3, 10)

        cart_added = False
        converted = False

        # App open
        events.append([event_id, user_id, session_start, "app_open", session_id, city, device])
        event_id += 1

        for i in range(num_events):

            event_time = session_start + timedelta(minutes=i*random.randint(1, 3))
            event_name = random.choices(
                EVENT_POOL,
                weights=[3, 3, 4, 2, 3],  # more browsing, fewer cart adds
                k=1)[0]


            if event_name == "add_to_cart":
                cart_added = True

            # Abandon cart logic
            if cart_added and random.random() < 0.15: #NOTE: changed from 0.3 to 0.15
                events.append([event_id, user_id, event_time, "checkout_start", session_id, city, device])
                event_id += 1

                r = random.random()

                if r < 0.05:
                    # 5% failure
                    events.append([event_id, user_id, event_time, "payment_failed", session_id, city, device])
                    event_id += 1
                    break

                elif r < 0.75:
                    # 70% success
                    events.append([event_id, user_id, event_time, "payment_success", session_id, city, device])
                    event_id += 1

                    events.append([event_id, user_id, event_time, "order_placed", session_id, city, device])
                    event_id += 1

                    converted = True
                    break

                else:
                    # 25% abandon at checkout
                    break
            events.append([event_id, user_id, event_time, event_name, session_id, city, device])
            event_id += 1

        # App close
        events.append([event_id, user_id, event_time + timedelta(minutes=1), "app_close", session_id, city, device])
        event_id += 1

        # Order table
        if converted:
            delivery_time = max(5, int(np.random.normal(18, 6)))
            discount_used = random.random() < 0.4
            order_value = round(np.random.normal(600, 200), 2)

            orders.append([
                order_id,
                user_id,
                session_start,
                order_value,
                delivery_time,
                random.choice(["UPI", "Card", "COD"]),
                discount_used,
                city
            ])
            order_id += 1

            # Churn logic
            if delivery_time > 30 and random.random() < 0.4:
                churned = True

        last_active = session_start

# -----------------------------
# SAVE
# -----------------------------

events_df = pd.DataFrame(events, columns=[
    "event_id", "user_id", "event_time",
    "event_name", "session_id",
    "city", "device_type"
])

orders_df = pd.DataFrame(orders, columns=[
    "order_id", "user_id", "order_time",
    "order_value", "delivery_time_minutes",
    "payment_method", "is_discount_used", "city"
])

users_df.to_csv("users.csv", index=False)
events_df.to_csv("events.csv", index=False)
orders_df.to_csv("orders.csv", index=False)

print("Done.")
print("Users:", len(users_df))
print("Events:", len(events_df))
print("Orders:", len(orders_df))
