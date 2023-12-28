"""-able vs. -ible."""

from __future__ import annotations

from proselint.tools import ResultCheck, memoize, preferred_forms_check


@memoize
def check(text: str) -> list[ResultCheck]:
    """-able vs. -ible."""
    err = "spelling.able_ible"
    msg = "-able vs. -ible. '{}' is the preferred spelling."

    preferences = [

        ["actionable",      ["actionible"]],
        ["addable",         ["addible"]],
        ["admittable",      ["admittible"]],
        ["advisable",       ["advisible"]],
        ["affectable",      ["affectible"]],
        ["allegeable",      ["allegeible"]],
        ["analyzable",      ["analyzible"]],
        ["annexable",       ["annexible"]],
        ["arrestable",      ["arrestible"]],
        ["ascendable",      ["ascendible"]],
        ["assertable",      ["assertible"]],
        ["assessable",      ["assessible"]],
        ["averageable",     ["averageible"]],
        ["bailable",        ["bailible"]],
        ["blamable",        ["blamible"]],
        ["changeable",      ["changeible"]],
        ["chargeable",      ["chargeible"]],
        ["circumscribable", ["circumscribible"]],
        ["commensurable",   ["commensurible"]],
        ["committable",     ["committible"]],
        ["condensable",     ["condensible"]],
        ["connectable",     ["connectible"]],
        ["contestable",     ["contestible"]],
        ["contractable",    ["contractible"]],
        ["conversable",     ["conversible"]],
        ["convictable",     ["convictible"]],
        ["correctable",     ["correctible"]],
        ["definable",       ["definible"]],
        ["detectable",      ["detectible"]],
        ["diagnosable",     ["diagnosible"]],
        ["discussable",     ["discussible"]],
        ["endorsable",      ["endorsible"]],
        ["enforceable",     ["enforceible"]],
        ["evadable",        ["evadible"]],
        ["excisable",       ["excisible"]],
        ["excludable",      ["excludible"]],
        ["expandable",      ["expandible"]],
        ["extendable",      ["extendible"]],
        ["extractable",     ["extractible"]],
        ["ignitable",       ["ignitible"]],
        ["immovable",       ["immovible"]],
        ["improvable",      ["improvible"]],
        ["includable",      ["includible"]],
        ["inferable",       ["inferible"]],
        ["inventable",      ["inventible"]],
        ["investable",      ["investible"]],
        ["lapsable",        ["lapsible"]],
        ["lovable",         ["lovible"]],
        ["mixable",         ["mixible"]],
        ["movable",         ["movible"]],
        ["noticeable",      ["noticeible"]],
        ["offendable",      ["offendible"]],
        ["patentable",      ["patentible"]],
        ["persuadable",     ["persuadible"]],
        ["preventable",     ["preventible"]],
        ["processable",     ["processible"]],
        ["protectable",     ["protectible"]],
        ["ratable",         ["ratible"]],
        ["redressable",     ["redressible"]],
        ["referable",       ["referible"]],
        ["retractable",     ["retractible"]],
        ["revisable",       ["revisible"]],
        ["rinsable",        ["rinsible"]],
        ["salable",         ["salible"]],
        ["suspendable",     ["suspendible"]],
        ["tractable",       ["tractible"]],
        ["transferable",    ["transferible"]],
        ["transmittable",   ["transmittible"]],
        ["willable",        ["willible"]],

        ["accessible",      ["accessable"]],
        ["adducible",       ["adducable"]],
        ["admissible",      ["admissable"]],
        ["audible",         ["audable"]],
        ["avertible",       ["avertable"]],
        ["collapsible",     ["collapsable"]],
        ["collectible",     ["collectable"]],
        ["combustible",     ["combustable"]],
        ["compactible",     ["compactable"]],
        ["compatible",      ["compatable"]],
        ["comprehensible",  ["comprehensable"]],
        ["compressible",    ["compressable"]],
        ["concussible",     ["concussable"]],
        ["conductible",     ["conductable"]],
        ["contemptible",    ["contemptable"]],
        ["controvertible",  ["controvertable"]],
        ["convertible",     ["convertable"]],
        ["corrodible",      ["corrodable"]],
        ["corruptible",     ["corruptable"]],
        ["credible",        ["credable"]],
        ["deducible",       ["deducable"]],
        ["deductible",      ["deductable"]],
        ["defeasible",      ["defeasable"]],
        ["defensible",      ["defensable"]],
        ["descendible",     ["descendable"]],
        ["destructible",    ["destructable"]],
        ["diffusible",      ["diffusable"]],
        ["digestible",      ["digestable"]],
        ["discernible",     ["discernable"]],
        ["dismissible",     ["dismissable"]],
        ["divisible",       ["divisable"]],
        ["edible",          ["edable"]],
        ["educible",        ["educable"]],
        ["eligible",        ["eligable"]],
        ["erodible",        ["erodable"]],
        ["exhaustible",     ["exhaustable"]],
        ["expressible",     ["expressable"]],
        ["fallible",        ["fallable"]],
        ["feasible",        ["feasable"]],
        ["flexible",        ["flexable"]],
        ["forcible",        ["forcable"]],
        ["fusible",         ["fusable"]],
        ["gullible",        ["gullable"]],
        ["horrible",        ["horrable"]],
        ["impressible",     ["impressable"]],
        ["inadmissible",    ["inadmissable"]],
        ["incorrigible",    ["incorrigable"]],
        ["indelible",       ["indelable"]],
        ["inexpressible",   ["inexpressable"]],
        ["intelligible",    ["intelligable"]],
        ["interfusible",    ["interfusable"]],
        ["invincible",      ["invincable"]],
        ["irascible",       ["irascable"]],
        ["irresistible",    ["irresistable"]],
        ["legible",         ["legable"]],
        ["negligible",      ["negligable"]],
        ["omissible",       ["omissable"]],
        ["oppressible",     ["oppressable"]],
        ["ostensible",      ["ostensable"]],
        ["perceptible",     ["perceptable"]],
        ["perfectible",     ["perfectable"]],
        ["permissible",     ["permissable"]],
        ["plausible",       ["plausable"]],
        ["possible",        ["possable"]],
        ["producible",      ["producable"]],
        ["reducible",       ["reducable"]],
        ["remissible",      ["remissable"]],
        ["reprehensible",   ["reprehensable"]],
        ["repressible",     ["repressable"]],
        ["resistible",      ["resistable"]],
        ["responsible",     ["responsable"]],
        ["reversible",      ["reversable"]],
        ["revertible",      ["revertable"]],
        ["risible",         ["risable"]],
        ["seducible",       ["seducable"]],
        ["sensible",        ["sensable"]],
        ["submersible",     ["submersable"]],
        ["submergible",     ["submergable"]],
        ["suggestible",     ["suggestable"]],
        ["suppressible",    ["suppressable"]],
        ["susceptible",     ["susceptable"]],
        ["terrible",        ["terrable"]],
        ["transfusible",    ["transfusable"]],
        ["transmissible",   ["transmissable"]],
        ["uncollectible",   ["uncollectable"]],
        ["vendible",        ["vendable"]],
        ["visible",         ["visable"]],
    ]

    return preferred_forms_check(text, preferences, err, msg)
