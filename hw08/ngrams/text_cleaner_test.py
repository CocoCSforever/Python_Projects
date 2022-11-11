from text_cleaner import TextCleaner


def test_process():
    """Test the process method"""
    tc = TextCleaner("Test")
    assert tc.process("Mr..") == "mr."
    assert tc.process("Mr. Rec, I am good.") == "mr rec COMMA i\
 am good."
    assert tc.process("I won't stay up today.") == "i won't stay up\
 today."
    assert tc.process("I won'%t (stay up) today. --Ms. Ma") == "i won't stay\
 up today. ms ma"
    assert tc.process("It's a Dead Scene, but That's a Good Thing") == "it's a\
 dead scene COMMA but that's a good thing"
    assert tc.process("By MANOHLA DARGIS (New York Times)") == "by manohla\
 dargis new york times"
