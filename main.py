from cards import CardManager
import sys

cm = CardManager()

print("Collecting JSON objects")
cm.get_json_file()

print("Beginning image scrape")
cm.process_json()

print("Operation completed")
