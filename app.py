import streamlit as st

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="MiniStore",
    page_icon="🛍️",
    layout="wide"
)

# ---------------------------------------------------
# Custom CSS
# ---------------------------------------------------
st.markdown("""
<style>
/* App-wide Styling */
.stApp {
    background-color: #f7f9fc;
}

/* Hero Banner */
.hero {
    background: linear-gradient(135deg, #4F46E5, #7C3AED);
    padding: 40px;
    border-radius: 15px;
    color: white;
    text-align: center;
    margin-bottom: 25px;
}

/* Text Element Styling inside Native Containers */
.product-title {
    font-size: 18px;
    font-weight: bold;
    color: #1F2937;
    margin-bottom: 2px;
}

.product-category {
    color: #6B7280;
    font-size: 13px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 10px;
}

.product-description {
    color: #4B5563;
    font-size: 14px;
    height: 60px;
    overflow: hidden;
}

.product-price {
    color: #4F46E5;
    font-size: 22px;
    font-weight: bold;
    margin-top: 10px;
    margin-bottom: 15px;
}

/* Floating support button */
.support-btn {
    position: fixed;
    bottom: 30px;
    right: 30px;
    background: #4F46E5;
    color: white !important;
    padding: 15px 25px;
    border-radius: 50px;
    text-decoration: none;
    font-weight: bold;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
    z-index: 999;
    transition: transform 0.2s;
}
.support-btn:hover {
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Product Data
# ---------------------------------------------------
products = [
    {
        "name": "Wireless Bluetooth Headphones",
        "price": 89.99,
        "category": "Electronics",
        "description": "Premium over-ear headphones with noise cancellation and 30-hour battery life."
    },
    {
        "name": "Smart Fitness Watch",
        "price": 129.99,
        "category": "Electronics",
        "description": "Track workouts, heart rate, sleep, and daily activity."
    },
    {
        "name": "Ergonomic Office Chair",
        "price": 249.99,
        "category": "Furniture",
        "description": "Comfortable chair with lumbar support."
    },
    {
        "name": "Minimalist Backpack",
        "price": 59.99,
        "category": "Fashion",
        "description": "Stylish and durable backpack."
    },
    {
        "name": "Portable Coffee Maker",
        "price": 44.99,
        "category": "Home & Kitchen",
        "description": "Compact coffee maker for travel."
    },
    {
        "name": "LED Desk Lamp",
        "price": 34.99,
        "category": "Home & Kitchen",
        "description": "Modern LED lamp with adjustable brightness."
    }
]

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------
st.sidebar.title("🛍️ MiniStore")

categories = ["All"] + sorted(
    list(set(product["category"] for product in products))
)

selected_category = st.sidebar.selectbox(
    "Browse Categories",
    categories,
    key="category_selectbox"
)

st.sidebar.markdown("---")
st.sidebar.subheader("🛒 Shopping Cart")

st.sidebar.metric(
    "Items",
    3
)

st.sidebar.metric(
    "Total",
    "$224.97"
)

# ---------------------------------------------------
# Filter Products
# ---------------------------------------------------
if selected_category == "All":
    filtered_products = products
else:
    filtered_products = [
        product
        for product in products
        if product["category"] == selected_category
    ]

# ---------------------------------------------------
# Hero Section
# ---------------------------------------------------
st.markdown("""
<div class="hero">
<h1>🛍️ MiniStore</h1>
<p>Your one-stop destination for quality products.</p>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Welcome Section
# ---------------------------------------------------
st.header("Welcome to MiniStore")
st.write("Discover premium electronics, furniture, fashion and home essentials.")
st.markdown("---")

# ---------------------------------------------------
# Featured Products Grid
# ---------------------------------------------------
st.subheader("⭐ Featured Products")

# Create 3 columns for our store layout
cols = st.columns(3)

for i, product in enumerate(filtered_products):
    # Dynamically distribute cards into columns 0, 1, or 2
    with cols[i % 3]:
        # Using native st.container(border=True) acts as our crisp layout card
        with st.container(border=True):
            st.markdown(f'<div class="product-title">{product["name"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="product-category">{product["category"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="product-description">{product["description"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="product-price">${product["price"]}</div>', unsafe_allow_html=True)
            
            # Button is now perfectly aligned inside the native card element
            st.button("Add to Cart", key=f"cart_button_{i}", use_container_width=True)

# ---------------------------------------------------
# Floating Support Button
# ---------------------------------------------------
st.markdown(
    """
<a href="/Support_Chatbot" target="_self" class="support-btn">
💬 Support
</a>
""",
    unsafe_allow_html=True
)

# ---------------------------------------------------
# Footer
# ---------------------------------------------------
st.markdown("---")
st.caption("© 2026 MiniStore")