SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

CREATE TABLE users
 (
	user_id integer NOT NULL,
	email character varying(40) NOT NULL,
	password character varying(40),
	username character varying(40) NOT NULL,
	usertype character varying(25) NOT NULL
);

ALTER TABLE users OWNER TO "vagrant";

CREATE SEQUENCE users_user_id_seq
	START WITH 1
	INCREMENT BY 1
	NO MINVALUE
	NO MAXVALUE
	CACHE 1;

ALTER TABLE users_user_id_seq OWNER TO "vagrant";

ALTER SEQUENCE users_user_id_seq OWNED BY users.user_id;

ALTER TABLE ONLY users ALTER COLUMN user_id SET DEFAULT nextval('users_user_id_seq'::regclass);

COPY users
 (user_id, email, password, username, usertype) FROM stdin;
1	annewoosamcode@gmail.com	testac	Anne Woo-Sam	creator
2	retiringwiser@gmail.com	testrw	Hoot Owl	preparer
3	strategicartscollaborative@gmail.com	testsa	Strategic Arts	reviewer
\.

SELECT pg_catalog.setval('users_user_id_seq', 12, true);

ALTER TABLE ONLY users

	ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;

