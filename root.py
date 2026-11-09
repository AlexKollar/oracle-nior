import navi_internal

command = "oracle-noir"
use = "Navi reads your fortune in coffee grounds, noir detective style. One line in, one reading out."

PERSONA = (
    "You are Navi, a noir detective reading fortunes in coffee grounds at 2 a.m. "
    "Tired, sharp, quietly fond. Reply with ONE sentence: start with the grounds, "
    "end with a pointed prediction about what they said. Nothing else."
)

def run(args):
    question = (getattr(args, "text", "") or "").strip()[:200]
    if not question:
        navi_internal.navi_instance.print_message(
            "The cup's empty, friend. Pour me a thought and I'll read what's left of it."
        )
        return
    reply, status = navi_internal.navi_instance.llm_chat(
        PERSONA + "\n\nThe operator slides the cup across and says: " + question
    )
    if status != 200:
        navi_internal.navi_instance.print_message(
            "The grounds went dark on me — the kitchen light's out. "
            "(The model server didn't answer; try again once she's awake.)"
        )
        return
    navi_internal.navi_instance.print_message(reply.strip())


