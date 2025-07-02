def is_last_message_from_friend(chat_history: str, your_name: str) -> bool:
    # split lines
    lines = [line.strip() for line in chat_history.strip().split("\n") if line.strip()]
    
    for line in reversed(lines):
        if "]" in line and ":" in line:
            try:
                # Extract name part
                name_part = line.split("]")[1].split(":")[0].strip()
                # Compare ignoring case
                if name_part.lower() != your_name.lower():
                    return True
                else:
                    return False
            except Exception:
                continue
    return False


def get_last_line(chat_history: str) -> str:
    lines = [line.strip() for line in chat_history.strip().split("\n") if line.strip()]
    return lines[-1] if lines else ""