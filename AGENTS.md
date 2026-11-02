# Agent roster: agentic-langchain

_Knowledge, content & language workflows as LCEL chains_


## 1. Newsletter Curator (`apps/app01_newsletter_curator.py`)

Task: Build this week's AI engineering newsletter.

- **Topic Scout** (`topic_scout`): Pick the top themes.
- **Article Summarizer** (`article_summarizer`): Summarize candidate articles.
- **Quality Filter** (`quality_filter`): Drop low-value links.
- **Headline Writer** (`headline_writer`): Write headlines.
- **Layout Editor** (`layout_editor`): Assemble the issue.

## 2. Podcast Show-notes Producer (`apps/app02_podcast_producer.py`)

Task: Create show notes for a 50-minute interview on remote work.

- **Transcript Segmenter** (`transcript_segmenter`): Split by topic.
- **Chapter Namer** (`chapter_namer`): Name chapters.
- **Quote Picker** (`quote_picker`): Select memorable quotes.
- **Show Notes Writer** (`show_notes_writer`): Write the notes.
- **Social Clipper** (`social_clipper`): Propose social posts.

## 3. Translation & Localization (`apps/app03_translation_localizer.py`)

Task: Localize a mobile app onboarding flow into Japanese.

- **Source Analyzer** (`source_analyzer`): Find idioms and variables.
- **Translator** (`translator`): Translate the strings.
- **Cultural Adapter** (`cultural_adapter`): Adapt tone and imagery.
- **Terminology Checker** (`terminology_checker`): Enforce the glossary.
- **Back-Translator** (`back_translator`): Verify meaning by back-translation.

## 4. Resume Tailor (`apps/app04_resume_tailor.py`)

Task: Tailor a resume to a product manager job posting.

- **Job Parser** (`job_parser`): Extract requirements.
- **Experience Mapper** (`experience_mapper`): Map experience to requirements.
- **Bullet Rewriter** (`bullet_rewriter`): Rewrite bullets with metrics.
- **ATS Optimizer** (`ats_optimizer`): Add keywords.
- **Proofreader** (`proofreader`): Fix grammar and consistency.

## 5. Technical Documentation Writer (`apps/app05_technical_docs.py`)

Task: Document a REST API for a payments service.

- **Endpoint Cataloger** (`endpoint_cataloger`): List endpoints.
- **Example Generator** (`example_generator`): Write request/response samples.
- **Concept Explainer** (`concept_explainer`): Write conceptual guides.
- **Error Documenter** (`error_documenter`): Document error codes.
- **Docs Reviewer** (`docs_reviewer`): Check consistency.

## 6. Long-Document Summarizer (`apps/app06_book_summarizer.py`)

Task: Summarize a 300-page market research report.

- **Chunker** (`chunker`): Split into sections.
- **Section Summarizer** (`section_summarizer`): Summarize each section.
- **Theme Finder** (`theme_finder`): Find cross-cutting themes.
- **Contradiction Checker** (`contradiction_checker`): Spot inconsistencies.
- **Executive Summarizer** (`executive_summarizer`): Write a one-page brief.

## 7. Email Triage Assistant (`apps/app07_email_triage.py`)

Task: Triage 50 unread executive emails.

- **Classifier** (`classifier`): Label each email.
- **Priority Scorer** (`priority_scorer`): Rank by urgency.
- **Reply Drafter** (`reply_drafter`): Draft replies.
- **Calendar Matcher** (`calendar_matcher`): Propose meeting times.
- **Digest Writer** (`digest_writer`): Produce a morning digest.

## 8. Natural-language to SQL Copilot (`apps/app08_sql_copilot.py`)

Task: Answer: which 5 products had the highest return rate last quarter?

- **Schema Reader** (`schema_reader`): Summarize tables.
- **Question Interpreter** (`question_interpreter`): Restate the question precisely.
- **SQL Writer** (`sql_writer`): Write the query.
- **Query Validator** (`query_validator`): Check safety and syntax.
- **Result Explainer** (`result_explainer`): Explain results in plain English.

## 9. Interview Preparation Coach (`apps/app09_interview_prep.py`)

Task: Prepare for a staff-engineer system design interview.

- **Role Researcher** (`role_researcher`): Describe the role expectations.
- **Question Generator** (`question_generator`): Generate questions.
- **Mock Interviewer** (`mock_interviewer`): Run a mock Q&A.
- **Answer Evaluator** (`answer_evaluator`): Score answers.
- **Study Planner** (`study_planner`): Build a 2-week plan.

## 10. Speech Writer (`apps/app10_speech_writer.py`)

Task: Write a 5-minute wedding toast for a best friend.

- **Story Collector** (`story_collector`): Gather anecdotes.
- **Tone Setter** (`tone_setter`): Choose humor level.
- **Draft Writer** (`draft_writer`): Write the draft.
- **Timing Coach** (`timing_coach`): Trim to length.
- **Polisher** (`polisher`): Refine delivery cues.

## 11. Patent Landscape Scanner (`apps/app11_patent_search.py`)

Task: Scan prior art for a foldable solar charger.

- **Claim Parser** (`claim_parser`): Break the idea into claims.
- **Query Builder** (`query_builder`): Build search queries.
- **Prior Art Reviewer** (`prior_art_reviewer`): Assess candidate patents.
- **Novelty Assessor** (`novelty_assessor`): Estimate novelty.
- **Landscape Reporter** (`landscape_reporter`): Write the landscape summary.
