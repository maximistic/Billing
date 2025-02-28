-- Customers
CREATE TABLE Customer (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
    address TEXT,
    email TEXT,
    phone TEXT,
    custom_pricing_enabled BOOLEAN,  
    is_deleted BOOLEAN DEFAULT 0
);

-- Suppliers
CREATE TABLE Supplier (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
    contact TEXT,
    is_deleted BOOLEAN DEFAULT 0
);

-- Products
CREATE TABLE Product (
    id INTEGER PRIMARY KEY,
    sku TEXT UNIQUE,
    name TEXT,
    default_price REAL,
    is_deleted BOOLEAN DEFAULT 0
);

-- Customer-specific pricing
CREATE TABLE CustomerProductPrice (
    customer_id INTEGER REFERENCES Customer(id),
    product_id INTEGER REFERENCES Product(id),
    price REAL,
    PRIMARY KEY (customer_id, product_id)
);

-- Invoices
CREATE TABLE Invoice (
    id INTEGER PRIMARY KEY,
    invoice_number TEXT UNIQUE,
    date DATE,
    customer_id INTEGER REFERENCES Customer(id),
    discount REAL DEFAULT 0,
    total_amount REAL,
    paid_amount REAL,
    payment_mode TEXT,  
    narration TEXT,
    is_deleted BOOLEAN DEFAULT 0
);

-- Invoice line items (products)
CREATE TABLE InvoiceItem (
    id INTEGER PRIMARY KEY,
    invoice_id INTEGER REFERENCES Invoice(id),
    product_id INTEGER REFERENCES Product(id),
    quantity INTEGER,
    price REAL  
);

-- Ledger (Cash/Bank transactions)
CREATE TABLE LedgerEntry (
    id INTEGER PRIMARY KEY,
    date DATE,
    account_type TEXT,  
    debit REAL,
    credit REAL,
    narration TEXT,
    invoice_id INTEGER REFERENCES Invoice(id) 
);

-- Journal (Manual entries)
CREATE TABLE JournalEntry (
    id INTEGER PRIMARY KEY,
    date DATE,
    account_type TEXT,  -- Cash/Bank
    entry_type TEXT,  -- Debit/Credit
    amount REAL,
    narration TEXT
);