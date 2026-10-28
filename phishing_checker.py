
import re
from urllib.parse import urlparse


def inspect_url(raw_url):
    """Check a URL for selected phishing warning signs."""

    url = raw_url.strip()
    findings = []

    if not url:
        return ["No URL entered."]

    # Add a default scheme if the user does not enter one.
    candidate = url if "://" in url else "http://" + url

    try:
        parsed = urlparse(candidate)
    except ValueError:
        return ["This text is not a valid URL format."]

    host = (parsed.hostname or "").lower()

    if not host:
        return ["Could not identify a hostname."]

    # Check 1: Look for an @ symbol.
    if "@" in candidate:
        findings.append(
            "Contains an @ symbol; inspect carefully."
        )

    # Check 2: Check whether the URL is unusually long.
    if len(url) > 100:
        findings.append(
            "Unusually long URL (over 100 characters)."
        )

    # Check 3: Check whether the hostname is an IPv4 address.
    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append(
            "Uses an IP address instead of a familiar domain."
        )

    # Check 4: Check for many hostname segments.
    labels = [part for part in host.split(".") if part]

    if len(labels) >= 5:
        findings.append(
            "Contains many hostname segments/subdomains."
        )

    # Check 5: Check for a punycode-style hostname marker.
    if "xn--" in host:
        findings.append(
            "Contains a punycode-style hostname."
        )

    # Check 6: Check whether the URL uses HTTP.
    if parsed.scheme.lower() == "http":
        findings.append(
            "Uses HTTP. HTTPS alone does not prove trust."
        )

    # Display a message when no listed warning signs are found.
    if not findings:
        findings.append(
            "No listed warning signs found. "
            "This does NOT prove safety."
        )

    return findings


def main():
    print("=" * 45)
    print("   EWB PHISHING URL AWARENESS CHECKER")
    print("=" * 45)
    print("This program checks URL text only.")
    print("It does not open or visit websites.")

    # Repeat the program until the user chooses to quit.
    while True:
        raw_url = input(
            "\nEnter a sample URL (or type q to quit): "
        )

        if raw_url.strip().lower() in ("q", "quit", "exit"):
            print("\nThank you for using the checker!")
            print("Stay alert online.")
            break

        findings = inspect_url(raw_url)

        print("\n--- CHECK RESULTS ---")

        for item in findings:
            print("* " + item)

        # Show a summary if warning signs were found.
        info_starts = (
            "No URL entered",
            "Could not identify",
            "This text is not valid",
            "No listed warning signs"
        )

        has_warnings = not any(
            item.startswith(info_starts)
            for item in findings
        )

        if has_warnings:
            print(
                f"\nREVIEW CAREFULLY: "
                f"{len(findings)} warning sign(s) found."
            )

        print(
            "\nSafety reminder: Never enter passwords "
            "on suspicious websites."
        )


if __name__ == "__main__":
    main()
