"""
Database migration script to add template and font_size columns to projects table
"""
import sqlite3

def migrate():
    conn = sqlite3.connect('presentwallah.db')
    cursor = conn.cursor()
    
    # Check if columns already exist
    cursor.execute("PRAGMA table_info(projects)")
    columns = [col[1] for col in cursor.fetchall()]
    
    # Add template column if it doesn't exist
    if 'template' not in columns:
        print("Adding 'template' column...")
        cursor.execute("ALTER TABLE projects ADD COLUMN template VARCHAR(50) DEFAULT 'modern'")
        cursor.execute("UPDATE projects SET template = 'modern' WHERE template IS NULL")
        print("✓ Added 'template' column")
    else:
        print("✓ 'template' column already exists")
    
    # Add font_size column if it doesn't exist
    if 'font_size' not in columns:
        print("Adding 'font_size' column...")
        cursor.execute("ALTER TABLE projects ADD COLUMN font_size INTEGER DEFAULT 20")
        cursor.execute("UPDATE projects SET font_size = 20 WHERE font_size IS NULL")
        print("✓ Added 'font_size' column")
    else:
        print("✓ 'font_size' column already exists")
    
    conn.commit()
    conn.close()
    print("\nMigration complete!")

if __name__ == "__main__":
    migrate()
