-- The default postgres user will execute these commands
-- POSTGRES_USER, POSTGRES_PASSWORD, and POSTGRES_DB are automatically handled by the postgres image
-- We don't need to create them manually

-- Create the database if it doesn't exist
CREATE DATABASE ${POSTGRES_DB};

-- Connect to the new database
\c ${POSTGRES_DB}

-- Grant schema privileges to the default user
ALTER DEFAULT PRIVILEGES GRANT ALL ON TABLES TO ${POSTGRES_USER};
ALTER DEFAULT PRIVILEGES GRANT ALL ON SEQUENCES TO ${POSTGRES_USER};

-- Grant schema privileges
\c ${POSTGRES_DB}

-- Grant schema privileges to the default user
ALTER DEFAULT PRIVILEGES GRANT ALL ON TABLES TO ${POSTGRES_USER};
ALTER DEFAULT PRIVILEGES GRANT ALL ON SEQUENCES TO ${POSTGRES_USER};
ALTER DEFAULT PRIVILEGES GRANT ALL ON FUNCTIONS TO ${POSTGRES_USER}; 