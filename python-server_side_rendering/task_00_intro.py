#!/usr/bin/python3
"""Generate invitation files from a template and attendee data."""


PLACEHOLDERS = ("name", "event_title", "event_date", "event_location")


def generate_invitations(template, attendees):
    """Generate one invitation file per attendee."""
    if not isinstance(template, str):
        print(
            "Invalid input: template must be a string, "
            f"got {type(template).__name__}."
        )
        return

    if not isinstance(attendees, list):
        print(
            "Invalid input: attendees must be a list of dictionaries, "
            f"got {type(attendees).__name__}."
        )
        return

    if any(not isinstance(attendee, dict) for attendee in attendees):
        print(
            "Invalid input: attendees must be a list of dictionaries, "
            "found a non-dictionary item."
        )
        return

    if template == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        invitation = template

        for placeholder in PLACEHOLDERS:
            value = attendee.get(placeholder)
            if value is None:
                value = "N/A"
            else:
                value = str(value)
            invitation = invitation.replace("{" + placeholder + "}", value)

        output_file = f"output_{index}.txt"

        try:
            with open(output_file, "w", encoding="utf-8") as file:
                file.write(invitation)
        except OSError as exc:
            print(f"Error writing {output_file}: {exc}")
