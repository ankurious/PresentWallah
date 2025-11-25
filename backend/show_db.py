import sqlite3
from datetime import datetime

conn = sqlite3.connect('presentwallah.db')
cursor = conn.cursor()

print("\n" + "="*60)
print("  PRESENTWALLAH DATABASE STRUCTURE")
print("="*60)

print("\n📊 DATABASE TABLES:")
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
for row in cursor.fetchall():
    print(f"  ✓ {row[0]}")

print("\n" + "-"*60)
print("📝 SECTIONS TABLE (stores content, comments, feedback)")
print("-"*60)
cursor.execute('PRAGMA table_info(sections)')
for row in cursor.fetchall():
    print(f"  {row[1]:20} {row[2]}")

print("\n" + "-"*60)
print("📚 REVISIONS TABLE (stores all refinement history)")
print("-"*60)
cursor.execute('PRAGMA table_info(revisions)')
for row in cursor.fetchall():
    print(f"  {row[1]:20} {row[2]}")

# Show sample data if exists
print("\n" + "="*60)
print("  SAMPLE DATA")
print("="*60)

cursor.execute("SELECT COUNT(*) FROM sections")
section_count = cursor.fetchone()[0]
print(f"\n📄 Total Sections: {section_count}")

if section_count > 0:
    print("\nLatest Section:")
    cursor.execute("""
        SELECT id, title, 
               CASE WHEN liked=1 THEN '👍' WHEN liked=0 THEN '👎' ELSE '—' END as feedback,
               CASE WHEN comment!='' THEN '✓' ELSE '✗' END as has_comment
        FROM sections 
        ORDER BY id DESC 
        LIMIT 1
    """)
    row = cursor.fetchone()
    print(f"  ID: {row[0]}")
    print(f"  Title: {row[1]}")
    print(f"  Feedback: {row[2]}")
    print(f"  Has Comment: {row[3]}")

cursor.execute("SELECT COUNT(*) FROM revisions")
revision_count = cursor.fetchone()[0]
print(f"\n📚 Total Revisions: {revision_count}")

if revision_count > 0:
    print("\nLatest Revision:")
    cursor.execute("""
        SELECT id, section_id, 
               substr(prompt, 1, 50) as prompt_preview,
               created_at
        FROM revisions 
        ORDER BY id DESC 
        LIMIT 1
    """)
    row = cursor.fetchone()
    if row:
        print(f"  Revision ID: {row[0]}")
        print(f"  Section ID: {row[1]}")
        print(f"  Prompt: {row[2]}...")
        print(f"  Created: {row[3]}")

print("\n" + "="*60)
print("  HOW IT WORKS")
print("="*60)
print("""
1. When you refine content:
   ✓ Old content saved in 'revisions.previous_content'
   ✓ Prompt saved in 'revisions.prompt'
   ✓ New content saved in 'revisions.new_content'
   ✓ Section updated with new content

2. When you add feedback:
   ✓ Like/Dislike stored in 'sections.liked'
   ✓ Comments stored in 'sections.comment'

3. Full history maintained for every refinement!
""")

conn.close()
