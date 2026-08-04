# Open Questions for Stakeholders

> **Update (2026-06-15):** Corrections implementation applied in-repo with executive defaults where noted. See [`executive_defaults.md`](executive_defaults.md) and [`workbook_patches/README.md`](workbook_patches/README.md). Items below remain for **formal stakeholder confirmation** — defaults can be reversed.

These questions arose during analysis. They are grouped by topic. Many come directly from the workbook's own Notes tab and from yellow/green-highlighted "needs confirmation" cells; others are inconsistencies found while reconciling the tabs.

---

## A. Ambiguous acronyms and terms

1. **SNAS** — What does SNAS stand for? The workbook only defines it operationally ("SNAS criteria reached/not reached"). Full expansion and the actual criteria are undocumented.
2. **SLC** — What system is "SLC" (referenced in "access to campus and SLC system")? Confirm full name and which access rights it controls.
3. **OAS / OASIS** — Are these the same office, or two (Office of Admissions vs OASIS)? Confirm the exact owning office for admission evaluation.
4. **REC-0052 / REF-0002** — Confirm these reference numbers: REC-0052 (Manage Exit from the University) and REF-0002 (the documentation set under which statuses are defined; scholarship statuses are explicitly excluded from it).
5. **"M3"** — What does the "M3" milestone label in the tab names denote?
6. **Levels `UG`, `GS`, `SOL`** — Confirm these mean Undergraduate, Graduate School, School of Law. Only `IS` (Integrated School) is confirmable from context.

## B. Conflicting M3 vs Post-M3 WIP rules

7. **Fee/process rename.** M3 used "Official Confirmation" and "Enrollment Reservation Fee"; Post-M3 renamed to "Official Acceptance" and "Official Acceptance Fee." Is the rename final, and should `A6.1`'s label be updated to match consistently?
8. **Deprecated applicant codes.** M3's `A3.3 Exam Not Required` and `A9.0 Inactive` are struck through. Confirm they are fully removed and that the "no Inactive status; conditions repurposed for data purge" decision is final.
9. **Deprecated student exit codes.** M3's `S3.5 Exited - Under Exclusion`, `S3.6 Exited - Expelled`, `S3.7 Inactive - Transferred` are struck through and apparently consolidated into `S4.2 Exited - Permanent Disqualification`. Confirm this consolidation is intended (it loses the distinction between exclusion, expulsion, and transfer).
10. **Prolonged Leave is new.** `S2.3 Inactive - Prolonged Leave` exists only in Post-M3 (highlighted). Confirm the exact thresholds: "LOA more than the maximum" and "last enrollment MORE than 6 trimesters ago" — and whether both must be true (AND) or either (OR).
11. **Program-status code renumbering.** The canonical program tab uses `P1.3 = Strict Probationary`, `P1.4 = Ineligible`; the M3 tab and the combination tab use `P1.3 = Ineligible` with no Strict Probationary code. Which numbering is final, and will the combination tab be re-coded to match?
12. **"Under Evaluation" / shifting.** M3 had a `P1.4 Under Evaluation` status for shifting applications; Post-M3 removed it in favor of a "Manage Shifting Application" process. Confirm shifting will never be a status.

## C. Terminal states

13. **Is `S4.0 Graduated` terminal?** Unlike `P3.0 Graduated` and the Exited statuses, the student status `S4.0 Graduated` is **not** labeled TERMINAL. Is this intentional (e.g. to support alumni / BS-to-MS continuation) or an oversight?
14. **`A5.4 Reconsidered` revives a terminal state.** `A5.4`'s only allowed previous is the terminal `A5.5 Not Qualified`. Should `A5.5` really be terminal, or should reconsideration branch before terminal rejection?
15. **`A7.0 Officially Admitted` labeled terminal.** Confirm this means "terminal for the admission application only" (it is the hand-off to Student Status), not the end of the person's journey.
16. **Terminal exits only allow `Incomplete`.** In the combination tab, every terminal student exit (`S3.4`–`S3.7`) pairs only with program status `P3.1 Incomplete`. Confirm no terminal-exit student can retain `Graduated` on a completed program.

## D. Future-state-only statuses

17. **Strict Probationary as a separate status.** The program tab explicitly weighs "Option 1: separate Strict Probationary status" vs "Option 2: fold into Probationary." Post-M3 appears to choose Option 1 (IS-only `P1.3`). Confirm this is the agreed decision.
18. **SAP grade criteria not finalized.** The note flags *"'below 75' needs to be updated"* and a worked Grade 1/2/3 example marked *"kindly confirm if correct."* What are the actual SAP grade thresholds?
19. **"Probationary for new students" vs "IS: both new and old."** Confirm the rule that Probationary is for new students generally, but for IS it applies to both new and old students.
20. **SAP students "asked to withdraw" → Ineligible.** The note says a failing SAP student "will be asked to withdraw" and adds "should be ineligible." Confirm SAP failure maps to `P1.4 Ineligible`.

## E. LOA, access, and clearance holds

21. **LOA campus/system access.** Notes #8: *"Students on LOA, will they be allowed access to campus, and systems?"* `S2.2 Under LOA` is classified Active (Active = full access per Notes), which seems to contradict "limited access when inactive." What is the actual access policy for LOA students?
22. **LOA + Probationary contradiction.** Notes #3 tentatively says a student "cannot have Under LOA + Probationary," but the combination tab marks `S2.2 Under LOA × P1.1 Probationary` as **Yes**. Which is correct?
23. **Graduated with clearance hold.** Notes #7: *"Graduated, but still with Clearance Hold. Should this be a separate status?"* Currently not modeled. Decision needed.
24. **Clearance hold mechanics.** Notes #4: holds are "an outcome of the conditions." Confirm whether a clearance hold is a separate flag/attribute rather than a status, and how it interacts with Graduated / Exited.

## F. BS/MS and program-after-graduation behavior

25. **BS/MS post-graduation.** Notes #6: *"Future-state — will there still be a BS/MS program? If yes, what will be the Student Status after they achieve Program Status Graduated? For existing BS/MS students, will they be asked to shift?"* Needs a decision on student status for ladderized/BS-MS programs after one stage graduates.

## G. Statuses vs separate processes / types

26. **Scholarship.** Notes #5: scholarship "will have a status but in a scholarship process; not documented under REF-0002." Confirm scholarship is out of scope for this status model.
27. **Foreign exchange (inbound/outbound), cross-enrollee, transferee.** Confirmed as student *types*, not statuses. Confirm these are captured as attributes elsewhere ("On exchange program? Yes/No").
28. **Shifting and Optional Minor Program.** Confirmed as processes ("Manage Shifting Application," "Apply for an Optional Minor Program"), not statuses. Confirm.

## H. AND/OR logic that needs clarification

29. **`A6.0 Reserved` conditions.** "Acceptance period not lapsed AND (fee paid OR fee waived)." Confirm the grouping — is it `(not lapsed) AND (paid OR waived)`?
30. **`S2.0 Active` "during term breaks" branch.** The condition "Is Active AND during term/semester breaks until last day of late enrollment and student did not enroll" keeps a non-enrolled student Active during the grace period. Confirm the exact boundary at which it flips to AWOL.
31. **`P1.1 Probationary` multi-source triggers.** Probationary can come from (a) a probationary admission offer, (b) old student + academic standards not complied, or (c) probation requirements not complied. Confirm these are all the same `P1.1` and how they differ in treatment.
32. **`A4.3 Further Evaluation Required` dual trigger.** It is triggered by both "exam not required" and "further screening required." Are these truly one status?

## I. Missing or ambiguous transition paths

33. **Allowed-previous lists imply, but don't draw, transitions.** The matrices give "allowed previous statuses," not explicit forward arrows. Confirm the implied forward transitions in the diagrams (especially returnee → `S1.0`, suspension → `S2.0`, and all program-status recoveries) are correct.
34. **Return from Suspension / Prolonged Leave.** `S2.0 Active` lists `S3.2` as an allowed previous, implying suspended students can return to Active. Confirm the re-entry path and whether `S2.3 Prolonged Leave` can return directly to `S2.0` or must pass through `S1.0`.
35. **Re-application after terminal rejection.** Can an applicant in a terminal `Not Qualified` state start a brand-new application (a new `A0`)? The model treats these as terminal for the *application*, but a person may re-apply.
36. **Combination tab vs status tabs reconciliation.** The combination matrix should be regenerated once the canonical student/program code schemes are finalized, since it currently uses outdated codes (`S3.x` exits, `P1.3 = Ineligible`).
37. **`S2.1 Active - Residency` allowed-previous.** Residency lists only `S2.0` as previous; confirm whether a student can go on LOA from Residency and back, and how Residency ends (to `S2.0`, graduation, or exit).
