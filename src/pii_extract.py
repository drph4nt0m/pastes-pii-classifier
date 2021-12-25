import json
import datetime
from commonregex import CommonRegex

skip = [
    "pastebin_com:T7hKXVi0",
    "pastebin_com:8ceCwTaX",
    # "stronghold_onion:pmou8sa5t",
    "pastebin_com:tnimTjk9",
    "pastebin_com:CGeXJxcA",
    "stronghold_onion:pwuqfwp4k",
    "pastebin_com:D6f6QXEd",
]

score = {"email": 3, "phone": 4, "ip": 3, "ipv6": 4, "credit_card": 5, "btc_address": 2}

with open("pastes.json", "r", encoding="utf-8") as pastes_f:
    pastes = json.load(pastes_f)

    piis = []

    stats = {}
    sites = {}
    scores = {}

    for i, paste in enumerate(pastes):
        print(f"{datetime.datetime.now()} [{paste['id']}] {i + 1}/{len(pastes)}")

        if paste["id"] in skip:
            print(f"Skipping {paste['id']}")
            continue

        parsed_text = CommonRegex(paste["paste"]["body"])
        pii = (
            [{"type": "email", "value": p} for p in list(set(parsed_text.emails)) if p]
            + [
                {"type": "phone", "value": p}
                for p in list(set(parsed_text.phones))
                if p
            ]
            + [{"type": "ip", "value": p} for p in list(set(parsed_text.ips)) if p]
            + [{"type": "ipv6", "value": p} for p in list(set(parsed_text.ipv6s)) if p]
            + [
                {"type": "credit_card", "value": p}
                for p in list(set(parsed_text.credit_cards))
                if p
            ]
            + [
                {"type": "btc_address", "value": p}
                for p in list(set(parsed_text.btc_addresses))
                if p
            ]
        )

        for x in ["email", "phone", "ip", "ipv6", "credit_card", "btc_address"]:
            if paste["site_id"] not in stats:
                stats[paste["site_id"]] = {}

            if x not in stats[paste["site_id"]]:
                stats[paste["site_id"]][x] = len(
                    [p for p in pii if p and p["type"] == x]
                )

            stats[paste["site_id"]][x] += len([p for p in pii if p and p["type"] == x])

        for p in pii:
            if p and p["type"] in score:
                if paste["site_id"] not in scores:
                    scores[paste["site_id"]] = {}

                if p["type"] not in scores[paste["site_id"]]:
                    scores[paste["site_id"]][p["type"]] = score[p["type"]]

                scores[paste["site_id"]][p["type"]] += score[p["type"]]

        if paste["site_id"] not in sites:
            sites[paste["site_id"]] = 0

        sites[paste["site_id"]] += 1

        piis.append(
            {"paste_id": paste["paste"]["id"], "site_id": paste["site_id"], "pii": pii}
        )

        if i % 200 == 0:
            with open("stats.json", "w") as stats_f:
                json.dump(stats, stats_f, indent=4)

            with open("sites.json", "w") as sites_f:
                json.dump(sites, sites_f, indent=4)

            with open("scores.json", "w") as scores_f:
                json.dump(scores, scores_f, indent=4)

    with open("stats.json", "w") as stats_f:
        json.dump(stats, stats_f, indent=4)

    with open("sites.json", "w") as sites_f:
        json.dump(sites, sites_f, indent=4)

    with open("scores.json", "w") as scores_f:
        json.dump(scores, scores_f, indent=4)

    with open("pii.json", "w") as pii_f:
        json.dump(piis, pii_f, indent=4)
