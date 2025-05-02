# Tunzaa Payment API (Python)

## Overview
The Tunzaa Payment API is a secure, FastAPI-based backend that enables users to create installment-based payment plans, save money weekly toward a product, and trigger a merchant payout when the savings target is reached. It supports JWT authentication, simulates weekly savings of TZS 5,000 toward a TZS 20,000 product, and includes a webhook for payment completion events. The API is modular, RESTful, and includes unit tests for core flows.

## What I Built
- **Core Functionality**:
  - **Payment Plans**: Users can create a payment plan for a product (TZS 20,000) and save TZS 5,000 weekly.
  - **Savings**: Users add savings to their plan, with automatic payout simulation (logged) when the target is reached.
  - **Authentication**: JWT-based authentication for secure user access to plans and savings.
  - **Webhook**: A POST endpoint (`/webhook/payment-completed`) to handle "payment completed" events.
- **Tech Stack**: FastAPI, SQLAlchemy (SQLite), Pydantic, python-jose, passlib, pytest.
- **Testing**: Unit tests for authentication (register/login) and payment flows (plan creation, savings, payout triggering).
- **Documentation**: Interactive Swagger UI at `/docs` for API exploration.

## Assumptions Made
- **Database**: SQLite is used for simplicity, with an in-memory database for tests. In production, a more robust database like PostgreSQL would be preferred.
- **Payout Simulation**: Payouts are logged to the console rather than integrated with a real payment gateway, as the challenge focuses on simulation.
- **Webhook**: The webhook endpoint logs events without signature verification, assuming a trusted source for this prototype. In production, signature verification would be added.
- **Currency**: All amounts are in TZS (Tanzanian Shillings) as per the challenge example.
- **Weekly Savings**: The TZS 5,000/week is a fixed example amount, but the API supports flexible savings amounts.

## How to Run
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/pmraushi/superteamengineeringchallenge.git
   cd superteamengineeringchallenge
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   Create a `.env` file in the root directory:
   ```env
   SECRET_KEY=secret-key
   DATABASE_URL=sqlite:///./tunzaa.db
   ```

4. **Run the Application**:
   ```bash
   uvicorn app.main:app --reload
   ```
   The API will be available at `http://localhost:8000`. Access Swagger UI at `http://localhost:8000/docs`.

5. **Run Tests**:
   ```bash
   pytest
   ```

## Design Choices
- **Modular Structure**: The codebase is organized into `api`, `core`, `models`, `schemas`, `crud`, `db`, and `tests` directories to ensure separation of concerns and scalability.
- **Financial Safety**: JWT authentication, database transactions, and input validation (via Pydantic) ensure secure and consistent financial operations.
- **Test Coverage**: Focused unit tests for authentication and payment flows to validate core functionality, with an in-memory database to isolate test environments.