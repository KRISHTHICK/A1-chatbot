import difflib

def categorize_changes(old_text, new_text):
    d = difflib.Differ()
    diff = list(d.compare(old_text.splitlines(), new_text.splitlines()))

    unchanged = []
    simple_changes = []
    large_changes = []
    completely_new = []

    for line in diff:
        if line.startswith('  '):
            unchanged.append(line[2:])
        elif line.startswith('- '):
            large_changes.append(line[2:])
        elif line.startswith('+ '):
            if line[2:] not in large_changes:
                completely_new.append(line[2:])
        elif line.startswith('? '):
            simple_changes.append(line[2:])
    
    return unchanged, simple_changes, large_changes, completely_new

def main():
    old_text = """Your old text goes here."""
    new_text = """Your new text goes here."""

    unchanged, simple_changes, large_changes, completely_new = categorize_changes(old_text, new_text)
    
    print("Unchanged lines:")
    for line in unchanged:
        print(line)
    
    print("\nSimple changes:")
    for line in simple_changes:
        print(line)
    
    print("\nLarge changes:")
    for line in large_changes:
        print(line)
    
    print("\nCompletely new lines:")
    for line in completely_new:
        print(line)

if __name__ == "__main__":
    main()
