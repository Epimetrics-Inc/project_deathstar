--
-- Create schema api in dev;
--
BEGIN;
CREATE SCHEMA api;
COMMIT;

--
-- Create model api.document
--
BEGIN;
CREATE TABLE api.document ("id" serial NOT NULL PRIMARY KEY, "created" timestamp with time zone NOT NULL, "modified" timestamp with time zone NOT NULL, "title" text, "date" date, "doctype" text, "docnum" text, "subject" text, "body" text, "sign" text, "signtitle" text, "images" jsonb, "raw_body" jsonb, "other_score" numeric(4, 2));
COMMIT;

--
-- Create model api.label with Foreign Key Constraint to api.document
--
BEGIN;
CREATE TABLE api.label ("created" timestamp with time zone NOT NULL, "modified" timestamp with time zone NOT NULL, "document_id" integer NOT NULL PRIMARY KEY, "mnchn_score" numeric(4, 2) NOT NULL, "adolescent_score" numeric(4, 2) NOT NULL, "specpop_score" numeric(4, 2) NOT NULL, "geriatric_score" numeric(4, 2) NOT NULL);
ALTER TABLE api.label ADD CONSTRAINT "api.label_document_id_fk_api.document_id" FOREIGN KEY ("document_id") REFERENCES api.document ("id") DEFERRABLE INITIALLY DEFERRED;
COMMIT;


--
-- Create roles and access privileges;
--
BEGIN;
CREATE ROLE web_anon nologin;

GRANT usage on schema api to web_anon;
grant select on api.document to web_anon;
grant select on api.label to web_anon;
COMMIT;


--
-- Create user authentication system;
--

-- We put things inside the basic_auth schema to hide
-- them from public view. Certain public procs/views will
-- refer to helpers and tables inside.
BEGIN;
create schema if not exists basic_auth;

create table if not exists
basic_auth.users (
  email    text primary key check ( email ~* '^.+@.+\..+$' ),
  pass     text not null check (length(pass) < 512),
  role     name not null check (length(role) < 512)
);


create or replace function
basic_auth.check_role_exists() returns trigger
  language plpgsql
  as $$
begin
  if not exists (select 1 from pg_roles as r where r.rolname = new.role) then
    raise foreign_key_violation using message =
      'unknown database role: ' || new.role;
    return null;
  end if;
  return new;
end
$$;

drop trigger if exists ensure_user_role_exists on basic_auth.users;

create constraint trigger ensure_user_role_exists
  after insert or update on basic_auth.users
  for each row
  execute procedure basic_auth.check_role_exists();

create extension if not exists pgcrypto;

create or replace function
basic_auth.encrypt_pass() returns trigger
  language plpgsql
  as $$

begin
  if tg_op = 'INSERT' or new.pass <> old.pass then
    new.pass = crypt(new.pass, gen_salt('bf'));
  end if;
  return new;
end
$$;

drop trigger if exists encrypt_pass on basic_auth.users;
create trigger encrypt_pass
  before insert or update on basic_auth.users
  for each row
  execute procedure basic_auth.encrypt_pass();

create or replace function
basic_auth.user_role(email text, pass text) returns name
  language plpgsql
  as $$

begin
  return (
  select role from basic_auth.users
   where users.email = user_role.email
     and users.pass = crypt(user_role.pass, users.pass)
  );
end;
$$;
COMMIT;
--
-- Create user login system;
--
CREATE EXTENSION if not exists pgjwt;

BEGIN;
CREATE TYPE basic_auth.jwt_token AS (
  token text
);

create or replace function
api.login(email text, pass text) returns basic_auth.jwt_token
  language plpgsql
  as $$
declare
  _role name;
  result basic_auth.jwt_token;
begin
  -- check email and password
  select basic_auth.user_role(email, pass) into _role;
  if _role is null then
    raise invalid_password using message = 'invalid user or password';
  end if;

  select sign(
      row_to_json(r), 'replaceinproductionplease'
    ) as token
    from (
      select _role as role, login.email as email,
         extract(epoch from now())::integer + 60*60 as exp
    ) r
    into result;
  return result;
end;
$$;

create role authenticator noinherit;
grant web_anon to authenticator;

grant usage on schema api, basic_auth to web_anon;
grant select on table pg_authid, basic_auth.users to web_anon;
grant execute on function api.login(text,text) to web_anon;


COMMIT;

--
-- For dev purposes only. UNCOMMENT;
--

BEGIN;
INSERT INTO basic_auth.users (email, pass, role) VALUES ('dev@dev.com', 'dev', 'dev');
COMMIT;