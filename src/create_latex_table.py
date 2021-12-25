import json

score = {"email": 1, "phone": 3, "ip": 1, "ipv6": 3, "credit_card": 5, "btc_address": 2}

with open("stats.json", "r", encoding="utf-8") as stats_f:
    stats = json.load(stats_f)

    for site in stats:
        print(
            f"""
{site}
\hline\hline
Email & {format(stats[site]["email"], ',d')} & {format(stats[site]["email"] * score["email"], ',d')} \\\\
\hline
Phone Number & {format(stats[site]["phone"], ',d')} & {format(stats[site]["phone"] * score["phone"], ',d')} \\\\
\hline
IPv4 Address & {format(stats[site]["ip"], ',d')} & {format(stats[site]["ip"] * score["ip"], ',d')} \\\\
\hline
IPv6 Address & {format(stats[site]["ipv6"], ',d')} & {format(stats[site]["ipv6"] * score["ipv6"], ',d')} \\\\
\hline
Credit Card Number & {format(stats[site]["credit_card"], ',d')} & {format(stats[site]["credit_card"] * score["credit_card"], ',d')} \\\\
\hline
Bitcoin Address & {format(stats[site]["btc_address"], ',d')} & {format(stats[site]["btc_address"] * score["btc_address"], ',d')} \\\\
\hline\hline
Total & {format(stats[site]["email"] + stats[site]["phone"] + stats[site]["ip"] + stats[site]["ipv6"] + stats[site]["credit_card"] + stats[site]["btc_address"], ',d')} & {format((stats[site]["email"]* score["email"]) + stats[site]["phone"] * score["phone"] + stats[site]["ip"] * score["ip"] + stats[site]["ipv6"] * score["ipv6"] + stats[site]["credit_card"] * score["credit_card"] + stats[site]["btc_address"] * score["btc_address"], ',d')} \\\\
"""
        )

        print(
            (
                stats[site]["email"] * score["email"]
                + stats[site]["phone"] * score["phone"]
                + stats[site]["ip"] * score["ip"]
                + stats[site]["ipv6"] * score["ipv6"]
                + stats[site]["credit_card"] * score["credit_card"]
                + stats[site]["btc_address"] * score["btc_address"]
            )
            / (
                stats[site]["email"]
                + stats[site]["phone"]
                + stats[site]["ip"]
                + stats[site]["ipv6"]
                + stats[site]["credit_card"]
                + stats[site]["btc_address"]
            )
        )
