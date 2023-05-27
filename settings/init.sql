CREATE DATABASE tl_bot_reminder;

\c tl_bot_reminder

CREATE TABLE public."user"(
	id UUID NOT NULL DEFAULT gen_random_uuid(),
	tl_user_id INTEGER NOT NULL,
	CONSTRAINT user_pk PRIMARY KEY(id)
);

CREATE TABLE public."event"(
    id UUID NOT NULL DEFAULT gen_random_uuid(),
    event_name VARCHAR(255) NOT NULL,
    event_date DATE NOT NULL,
    event_remind VARCHAR(16),
    event_remind_day_before BOOLEAN DEFAULT TRUE,
    user_id UUID NOT NULL,
    deleted INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT LOCALTIMESTAMP,
    CONSTRAINT event_pk PRIMARY KEY(id),
    CONSTRAINT fk_event FOREIGN KEY(user_id) REFERENCES public."user"(id)
);
