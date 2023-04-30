--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.24
-- Dumped by pg_dump version 9.6.24

-- Started on 2023-04-30 22:59:25

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 1 (class 3079 OID 12387)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 2564 (class 0 OID 0)
-- Dependencies: 1
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 192 (class 1259 OID 28026)
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO postgres;

--
-- TOC entry 191 (class 1259 OID 28024)
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO postgres;

--
-- TOC entry 2565 (class 0 OID 0)
-- Dependencies: 191
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- TOC entry 194 (class 1259 OID 28036)
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO postgres;

--
-- TOC entry 193 (class 1259 OID 28034)
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO postgres;

--
-- TOC entry 2566 (class 0 OID 0)
-- Dependencies: 193
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- TOC entry 190 (class 1259 OID 28018)
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO postgres;

--
-- TOC entry 189 (class 1259 OID 28016)
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO postgres;

--
-- TOC entry 2567 (class 0 OID 0)
-- Dependencies: 189
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- TOC entry 210 (class 1259 OID 28182)
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id bigint NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO postgres;

--
-- TOC entry 209 (class 1259 OID 28180)
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO postgres;

--
-- TOC entry 2568 (class 0 OID 0)
-- Dependencies: 209
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- TOC entry 188 (class 1259 OID 28008)
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO postgres;

--
-- TOC entry 187 (class 1259 OID 28006)
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO postgres;

--
-- TOC entry 2569 (class 0 OID 0)
-- Dependencies: 187
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- TOC entry 186 (class 1259 OID 27997)
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO postgres;

--
-- TOC entry 185 (class 1259 OID 27995)
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO postgres;

--
-- TOC entry 2570 (class 0 OID 0)
-- Dependencies: 185
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- TOC entry 242 (class 1259 OID 28507)
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO postgres;

--
-- TOC entry 226 (class 1259 OID 28268)
-- Name: mpo_bewoners; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.mpo_bewoners (
    id bigint NOT NULL,
    aanhef_bewoner character varying(30),
    achternaam_bewoner character varying(30),
    voorletters_bewoner character varying(30),
    phone_bewoner character varying(30),
    tussenvoegsels_bewoner character varying(30),
    email_bewoner character varying(254),
    site_id bigint NOT NULL
);


ALTER TABLE public.mpo_bewoners OWNER TO postgres;

--
-- TOC entry 225 (class 1259 OID 28266)
-- Name: mpo_bewoners_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.mpo_bewoners_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.mpo_bewoners_id_seq OWNER TO postgres;

--
-- TOC entry 2571 (class 0 OID 0)
-- Dependencies: 225
-- Name: mpo_bewoners_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.mpo_bewoners_id_seq OWNED BY public.mpo_bewoners.id;


--
-- TOC entry 231 (class 1259 OID 28318)
-- Name: mpo_boiler; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.mpo_boiler (
    inhoud integer,
    icem_id bigint NOT NULL
);


ALTER TABLE public.mpo_boiler OWNER TO postgres;

--
-- TOC entry 229 (class 1259 OID 28287)
-- Name: mpo_bouwkundig; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.mpo_bouwkundig (
    "nokHoogte" integer,
    "nokDiepte" integer,
    "typeDak" character varying(30),
    "positieBuitendeel" character varying(30),
    site_id bigint NOT NULL
);


ALTER TABLE public.mpo_bouwkundig OWNER TO postgres;

--
-- TOC entry 230 (class 1259 OID 28292)
-- Name: mpo_icem; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.mpo_icem (
    site_id bigint NOT NULL,
    "icemType" character varying(2),
    "energieModule" character varying(30),
    "positieIcem" character varying(30),
    aansluitingkanalen character varying(30),
    kwh_meter character varying(30),
    "sensoringOptie" character varying(255),
    type_prestatie character varying(30),
    koeling character varying(30),
    "positieWPmodule" character varying(30)
);


ALTER TABLE public.mpo_icem OWNER TO postgres;

--
-- TOC entry 232 (class 1259 OID 28323)
-- Name: mpo_icemdebiet; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.mpo_icemdebiet (
    stand1 integer,
    stand2 integer,
    stand3 integer,
    stand4 integer,
    stand5 integer,
    icem_id bigint NOT NULL
);


ALTER TABLE public.mpo_icemdebiet OWNER TO postgres;

--
-- TOC entry 233 (class 1259 OID 28328)
-- Name: mpo_omvormer; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.mpo_omvormer (
    "merkOmvormer" character varying(30),
    dakheling integer,
    capaciteit integer,
    owner boolean,
    levering_door boolean,
    levering_datum character varying(30),
    icem_id bigint NOT NULL
);


ALTER TABLE public.mpo_omvormer OWNER TO postgres;

--
-- TOC entry 234 (class 1259 OID 28333)
-- Name: mpo_planning; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.mpo_planning (
    bouwrouting integer,
    leverdatum character varying(30),
    icem_id bigint NOT NULL
);


ALTER TABLE public.mpo_planning OWNER TO postgres;

--
-- TOC entry 235 (class 1259 OID 28338)
-- Name: mpo_productiebonstatus; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.mpo_productiebonstatus (
    icem_id bigint NOT NULL,
    productiegereed character varying(30),
    "productieDatum" character varying(30)
);


ALTER TABLE public.mpo_productiebonstatus OWNER TO postgres;

--
-- TOC entry 236 (class 1259 OID 28343)
-- Name: mpo_productieexact; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.mpo_productieexact (
    "bomId" integer,
    exactnummer integer,
    icem_id bigint NOT NULL
);


ALTER TABLE public.mpo_productieexact OWNER TO postgres;

--
-- TOC entry 237 (class 1259 OID 28348)
-- Name: mpo_semkast; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.mpo_semkast (
    type character varying(30),
    icem_id bigint NOT NULL
);


ALTER TABLE public.mpo_semkast OWNER TO postgres;

--
-- TOC entry 228 (class 1259 OID 28278)
-- Name: mpo_site; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.mpo_site (
    id bigint NOT NULL,
    bouwnr character varying(30),
    blok character varying(30),
    straat character varying(30),
    huisnr character varying(10),
    postcode character varying(10),
    bijzonderheden text,
    koop_huur character varying(30),
    "projectId_id" bigint NOT NULL
);


ALTER TABLE public.mpo_site OWNER TO postgres;

--
-- TOC entry 227 (class 1259 OID 28276)
-- Name: mpo_site_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.mpo_site_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.mpo_site_id_seq OWNER TO postgres;

--
-- TOC entry 2572 (class 0 OID 0)
-- Dependencies: 227
-- Name: mpo_site_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.mpo_site_id_seq OWNED BY public.mpo_site.id;


--
-- TOC entry 238 (class 1259 OID 28353)
-- Name: mpo_warmtepomp; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.mpo_warmtepomp (
    vermogen double precision,
    icem_id bigint NOT NULL
);


ALTER TABLE public.mpo_warmtepomp OWNER TO postgres;

--
-- TOC entry 239 (class 1259 OID 28358)
-- Name: mpo_wtw; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.mpo_wtw (
    merk character varying(30),
    type character varying(30),
    debiet integer,
    icem_id bigint NOT NULL
);


ALTER TABLE public.mpo_wtw OWNER TO postgres;

--
-- TOC entry 241 (class 1259 OID 28412)
-- Name: opleverrapport_opleverrapport; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.opleverrapport_opleverrapport (
    id bigint NOT NULL,
    last_edit_datum character varying(30),
    druktest boolean NOT NULL,
    vacumeren boolean NOT NULL,
    datatest_npi_tool boolean NOT NULL,
    pragrammeren_warmtepomp boolean NOT NULL,
    "testHomecontroller" boolean NOT NULL,
    doorvoeren_afgedicht boolean NOT NULL,
    leiding_afgedopt boolean NOT NULL,
    reinigen_module boolean NOT NULL,
    visuele_inspectie_binnenzijde boolean NOT NULL,
    visuele_inspectie_buitenzijde boolean NOT NULL,
    bouwrouting_op_unit boolean NOT NULL,
    transportklarr_gemaakt boolean NOT NULL,
    router boolean NOT NULL,
    poe24v boolean NOT NULL,
    poe48v boolean NOT NULL,
    din_rail boolean NOT NULL,
    utp_kabel_groen boolean NOT NULL,
    utp_kabel_blauw boolean NOT NULL,
    utp_kabel_grijs boolean NOT NULL,
    utp_kabel_zwart boolean NOT NULL,
    boilersensor boolean NOT NULL,
    th1_kabel_display_kabel boolean NOT NULL,
    "homeController_set" boolean NOT NULL,
    omvormer boolean NOT NULL,
    sem_kast boolean NOT NULL,
    kwh_meter boolean NOT NULL,
    p5stekker_omvormer boolean NOT NULL,
    kampstrup_meter_21 boolean NOT NULL,
    landis_gyr_meter boolean NOT NULL,
    wtw boolean NOT NULL,
    soft_encloser boolean NOT NULL,
    tongdy boolean NOT NULL,
    procon boolean NOT NULL,
    antenne boolean NOT NULL,
    afvoer_flexbuis_slang boolean NOT NULL,
    sifon boolean NOT NULL,
    rode_sensor boolean NOT NULL,
    grijs_zwart_sensor boolean NOT NULL,
    aansluitslang_zwart boolean NOT NULL,
    lange_schroeven boolean NOT NULL,
    vilblokjes_oranje boolean NOT NULL,
    flow_sensor boolean NOT NULL,
    doorlock boolean NOT NULL,
    plexiplaat_e_module boolean NOT NULL,
    wielen boolean NOT NULL,
    opleverrapport_definitief boolean NOT NULL,
    opleverrapport_definitief_datum character varying(30),
    author_id bigint NOT NULL,
    project_id bigint NOT NULL,
    site_id bigint NOT NULL
);


ALTER TABLE public.opleverrapport_opleverrapport OWNER TO postgres;

--
-- TOC entry 240 (class 1259 OID 28410)
-- Name: opleverrapport_opleverrapport_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.opleverrapport_opleverrapport_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.opleverrapport_opleverrapport_id_seq OWNER TO postgres;

--
-- TOC entry 2573 (class 0 OID 0)
-- Dependencies: 240
-- Name: opleverrapport_opleverrapport_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.opleverrapport_opleverrapport_id_seq OWNED BY public.opleverrapport_opleverrapport.id;


--
-- TOC entry 212 (class 1259 OID 28206)
-- Name: project_klant; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.project_klant (
    id bigint NOT NULL,
    klantnaam character varying(30) NOT NULL,
    plaats character varying(30) NOT NULL,
    land character varying(30) NOT NULL,
    provincie character varying(30) NOT NULL,
    phone character varying(30) NOT NULL
);


ALTER TABLE public.project_klant OWNER TO postgres;

--
-- TOC entry 211 (class 1259 OID 28204)
-- Name: project_klant_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.project_klant_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.project_klant_id_seq OWNER TO postgres;

--
-- TOC entry 2574 (class 0 OID 0)
-- Dependencies: 211
-- Name: project_klant_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.project_klant_id_seq OWNED BY public.project_klant.id;


--
-- TOC entry 214 (class 1259 OID 28214)
-- Name: project_klantmedewerker; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.project_klantmedewerker (
    id bigint NOT NULL,
    name_medewerker character varying(30) NOT NULL,
    achternaam_medewerker character varying(30) NOT NULL,
    phone character varying(30) NOT NULL,
    functie_medewerker character varying(30) NOT NULL,
    "klantID_id" bigint NOT NULL
);


ALTER TABLE public.project_klantmedewerker OWNER TO postgres;

--
-- TOC entry 213 (class 1259 OID 28212)
-- Name: project_klantmedewerker_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.project_klantmedewerker_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.project_klantmedewerker_id_seq OWNER TO postgres;

--
-- TOC entry 2575 (class 0 OID 0)
-- Dependencies: 213
-- Name: project_klantmedewerker_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.project_klantmedewerker_id_seq OWNED BY public.project_klantmedewerker.id;


--
-- TOC entry 216 (class 1259 OID 28222)
-- Name: project_onderaanemerbedrijf; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.project_onderaanemerbedrijf (
    id bigint NOT NULL,
    naam character varying(30) NOT NULL
);


ALTER TABLE public.project_onderaanemerbedrijf OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 28220)
-- Name: project_onderaanemerbedrijf_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.project_onderaanemerbedrijf_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.project_onderaanemerbedrijf_id_seq OWNER TO postgres;

--
-- TOC entry 2576 (class 0 OID 0)
-- Dependencies: 215
-- Name: project_onderaanemerbedrijf_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.project_onderaanemerbedrijf_id_seq OWNED BY public.project_onderaanemerbedrijf.id;


--
-- TOC entry 218 (class 1259 OID 28230)
-- Name: project_project; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.project_project (
    id bigint NOT NULL,
    projectnr character varying(30) NOT NULL,
    projectnaam character varying(50) NOT NULL,
    plaats character varying(15) NOT NULL,
    provincie character varying(15) NOT NULL,
    land character varying(15) NOT NULL,
    "projectStatus" character varying(15) NOT NULL,
    offertenr character varying(30),
    exactnr character varying(30),
    debiteurnr character varying(30),
    renovatie_nieuwbouw character varying(15),
    "selectedWerkvoorbereiderFz" integer,
    "selectedProjecleiderFz" integer,
    inopdrachtvoor_vloerverwarming character varying(15),
    inopdrachtvoor_ventilatieinstallatie character varying(15),
    inopdrachtvoor_zonnepanelen character varying(15),
    "datumSystemInvoer" character varying(30),
    "startDatum" character varying(30),
    offertedatum character varying(30),
    "uitlijkDatumOpdrachtIndienWTW" character varying(30),
    "uitlijkDatumOpdrachtAlleenICEM" character varying(30),
    opmerking character varying(255),
    klant_id bigint NOT NULL
);


ALTER TABLE public.project_project OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 28228)
-- Name: project_project_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.project_project_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.project_project_id_seq OWNER TO postgres;

--
-- TOC entry 2577 (class 0 OID 0)
-- Dependencies: 217
-- Name: project_project_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.project_project_id_seq OWNED BY public.project_project.id;


--
-- TOC entry 220 (class 1259 OID 28243)
-- Name: project_projecticem; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.project_projecticem (
    id bigint NOT NULL,
    "iNumber" character varying(10) NOT NULL,
    "pNumber" character varying(10) NOT NULL,
    "eNumber" character varying(10) NOT NULL,
    "fNumber" character varying(10) NOT NULL,
    "aNumber" character varying(10) NOT NULL,
    "totaalNumber" character varying(20) NOT NULL,
    "estimatedValue" character varying(20) NOT NULL,
    project_id bigint NOT NULL
);


ALTER TABLE public.project_projecticem OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 28241)
-- Name: project_projecticem_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.project_projecticem_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.project_projecticem_id_seq OWNER TO postgres;

--
-- TOC entry 2578 (class 0 OID 0)
-- Dependencies: 219
-- Name: project_projecticem_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.project_projecticem_id_seq OWNED BY public.project_projecticem.id;


--
-- TOC entry 222 (class 1259 OID 28251)
-- Name: project_statusonderaanemer; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.project_statusonderaanemer (
    id bigint NOT NULL,
    status character varying(30) NOT NULL,
    odernummer character varying(30) NOT NULL,
    onderaanemer_id bigint,
    project_id_id bigint
);


ALTER TABLE public.project_statusonderaanemer OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 28249)
-- Name: project_statusonderaanemer_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.project_statusonderaanemer_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.project_statusonderaanemer_id_seq OWNER TO postgres;

--
-- TOC entry 2579 (class 0 OID 0)
-- Dependencies: 221
-- Name: project_statusonderaanemer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.project_statusonderaanemer_id_seq OWNED BY public.project_statusonderaanemer.id;


--
-- TOC entry 224 (class 1259 OID 28259)
-- Name: project_vertegenwoordiger_project; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.project_vertegenwoordiger_project (
    id bigint NOT NULL,
    projectnr character varying(30) NOT NULL,
    vertegenwoordiger_id bigint NOT NULL
);


ALTER TABLE public.project_vertegenwoordiger_project OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 28257)
-- Name: project_vertegenwoordiger_project_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.project_vertegenwoordiger_project_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.project_vertegenwoordiger_project_id_seq OWNER TO postgres;

--
-- TOC entry 2580 (class 0 OID 0)
-- Dependencies: 223
-- Name: project_vertegenwoordiger_project_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.project_vertegenwoordiger_project_id_seq OWNED BY public.project_vertegenwoordiger_project.id;


--
-- TOC entry 244 (class 1259 OID 28519)
-- Name: testrapport_testrapport; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.testrapport_testrapport (
    id bigint NOT NULL,
    last_edit_datum character varying(30),
    druktest boolean NOT NULL,
    druktest_datum character varying(30),
    luchtest boolean NOT NULL,
    luchtest_datum character varying(30),
    druk_cv character varying(30),
    flow_cv character varying(30),
    standtijd_cv character varying(30),
    druktap character varying(30),
    standtijd_druktap character varying(30),
    npidatatestuitgevoerd boolean NOT NULL,
    npidatatesuitgevoerd_datum character varying(30),
    "programmeerSD_kaart" boolean NOT NULL,
    aanvoertemp integer,
    tijd_legionella character varying(30),
    frame character varying(30),
    sem_gateway character varying(30),
    sem_mac_adres character varying(30),
    warmtepomp_binnen_ftc_unit character varying(30),
    warmtepomp_buiten character varying(30),
    procon character varying(30),
    ventilatie_wtw character varying(30),
    kamstrup_21_rond character varying(30),
    kamstrup_403_landis_t230 character varying(30),
    flowmeter character varying(30),
    display_mac_adres_homecontroller character varying(30),
    boiler character varying(30),
    spinvlies_voldoende boolean NOT NULL,
    bekabeling_voldoende boolean NOT NULL,
    lekvrij_door_blower_door_test boolean NOT NULL,
    spinvlies_zijkanten boolean NOT NULL,
    eindschoonmaak_binnenzijde boolean NOT NULL,
    stikstof_en_vacumeren_module character varying(30),
    stikstof_sterkte_bar character varying(30),
    stikstof_sterkte_standtijd character varying(30),
    vacumeren_module_micron character varying(30),
    vacumeren_module_standtijd character varying(30),
    lekdetectie boolean NOT NULL,
    lekdetectie_datum character varying(30),
    sn_label_op_frame boolean NOT NULL,
    wtw_debieten_control boolean NOT NULL,
    transportlabel_uitgevoerd boolean NOT NULL,
    eindschoonmaak_uitgevoerd boolean NOT NULL,
    transport_gereed boolean NOT NULL,
    transport_gereed_datum character varying(30),
    eindcontrole boolean NOT NULL,
    eindcontrole_datum character varying(30),
    testrapport_definitief boolean NOT NULL,
    testrapport_definitief_datum character varying(30),
    author_id bigint NOT NULL,
    project_id bigint NOT NULL,
    site_id bigint NOT NULL
);


ALTER TABLE public.testrapport_testrapport OWNER TO postgres;

--
-- TOC entry 243 (class 1259 OID 28517)
-- Name: testrapport_testrapport_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.testrapport_testrapport_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.testrapport_testrapport_id_seq OWNER TO postgres;

--
-- TOC entry 2581 (class 0 OID 0)
-- Dependencies: 243
-- Name: testrapport_testrapport_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.testrapport_testrapport_id_seq OWNED BY public.testrapport_testrapport.id;


--
-- TOC entry 196 (class 1259 OID 28070)
-- Name: users_customuser; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users_customuser (
    id bigint NOT NULL,
    password character varying(128) NOT NULL,
    is_superuser boolean NOT NULL,
    email character varying(254) NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    is_loggedin boolean NOT NULL,
    last_login timestamp with time zone NOT NULL,
    is_staff boolean NOT NULL,
    functie_id bigint NOT NULL
);


ALTER TABLE public.users_customuser OWNER TO postgres;

--
-- TOC entry 206 (class 1259 OID 28125)
-- Name: users_customuser_groups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users_customuser_groups (
    id bigint NOT NULL,
    customuser_id bigint NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.users_customuser_groups OWNER TO postgres;

--
-- TOC entry 205 (class 1259 OID 28123)
-- Name: users_customuser_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_customuser_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_customuser_groups_id_seq OWNER TO postgres;

--
-- TOC entry 2582 (class 0 OID 0)
-- Dependencies: 205
-- Name: users_customuser_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_customuser_groups_id_seq OWNED BY public.users_customuser_groups.id;


--
-- TOC entry 195 (class 1259 OID 28068)
-- Name: users_customuser_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_customuser_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_customuser_id_seq OWNER TO postgres;

--
-- TOC entry 2583 (class 0 OID 0)
-- Dependencies: 195
-- Name: users_customuser_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_customuser_id_seq OWNED BY public.users_customuser.id;


--
-- TOC entry 208 (class 1259 OID 28133)
-- Name: users_customuser_user_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users_customuser_user_permissions (
    id bigint NOT NULL,
    customuser_id bigint NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.users_customuser_user_permissions OWNER TO postgres;

--
-- TOC entry 207 (class 1259 OID 28131)
-- Name: users_customuser_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_customuser_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_customuser_user_permissions_id_seq OWNER TO postgres;

--
-- TOC entry 2584 (class 0 OID 0)
-- Dependencies: 207
-- Name: users_customuser_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_customuser_user_permissions_id_seq OWNED BY public.users_customuser_user_permissions.id;


--
-- TOC entry 204 (class 1259 OID 28112)
-- Name: users_functie; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users_functie (
    id bigint NOT NULL,
    functie character varying(30) NOT NULL,
    rol_id bigint NOT NULL
);


ALTER TABLE public.users_functie OWNER TO postgres;

--
-- TOC entry 203 (class 1259 OID 28110)
-- Name: users_functie_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_functie_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_functie_id_seq OWNER TO postgres;

--
-- TOC entry 2585 (class 0 OID 0)
-- Dependencies: 203
-- Name: users_functie_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_functie_id_seq OWNED BY public.users_functie.id;


--
-- TOC entry 198 (class 1259 OID 28080)
-- Name: users_klantwoningbouw; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users_klantwoningbouw (
    id bigint NOT NULL,
    name character varying(30) NOT NULL,
    phone_no character varying(128) NOT NULL,
    fax_number character varying(128) NOT NULL,
    straat character varying(30) NOT NULL,
    postcode character varying(30) NOT NULL,
    provincie character varying(30) NOT NULL,
    land character varying(30) NOT NULL
);


ALTER TABLE public.users_klantwoningbouw OWNER TO postgres;

--
-- TOC entry 197 (class 1259 OID 28078)
-- Name: users_klantwoningbouw_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_klantwoningbouw_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_klantwoningbouw_id_seq OWNER TO postgres;

--
-- TOC entry 2586 (class 0 OID 0)
-- Dependencies: 197
-- Name: users_klantwoningbouw_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_klantwoningbouw_id_seq OWNED BY public.users_klantwoningbouw.id;


--
-- TOC entry 202 (class 1259 OID 28099)
-- Name: users_medewerkerprofile; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users_medewerkerprofile (
    id bigint NOT NULL,
    voornaam character varying(30) NOT NULL,
    voorletter character varying(1),
    tussenvoegsel character varying(4),
    achternaam character varying(30) NOT NULL,
    geslacht character varying(30) NOT NULL,
    geboortdatum character varying(30) NOT NULL,
    phone_no character varying(255) NOT NULL,
    fax_number character varying(128) NOT NULL,
    user_id bigint NOT NULL
);


ALTER TABLE public.users_medewerkerprofile OWNER TO postgres;

--
-- TOC entry 201 (class 1259 OID 28097)
-- Name: users_medewerkerprofile_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_medewerkerprofile_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_medewerkerprofile_id_seq OWNER TO postgres;

--
-- TOC entry 2587 (class 0 OID 0)
-- Dependencies: 201
-- Name: users_medewerkerprofile_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_medewerkerprofile_id_seq OWNED BY public.users_medewerkerprofile.id;


--
-- TOC entry 200 (class 1259 OID 28088)
-- Name: users_role; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users_role (
    id bigint NOT NULL,
    role_name text NOT NULL
);


ALTER TABLE public.users_role OWNER TO postgres;

--
-- TOC entry 199 (class 1259 OID 28086)
-- Name: users_role_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_role_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_role_id_seq OWNER TO postgres;

--
-- TOC entry 2588 (class 0 OID 0)
-- Dependencies: 199
-- Name: users_role_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_role_id_seq OWNED BY public.users_role.id;


--
-- TOC entry 2198 (class 2604 OID 28029)
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- TOC entry 2199 (class 2604 OID 28039)
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- TOC entry 2197 (class 2604 OID 28021)
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- TOC entry 2207 (class 2604 OID 28185)
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- TOC entry 2196 (class 2604 OID 28011)
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- TOC entry 2195 (class 2604 OID 28000)
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- TOC entry 2216 (class 2604 OID 28271)
-- Name: mpo_bewoners id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mpo_bewoners ALTER COLUMN id SET DEFAULT nextval('public.mpo_bewoners_id_seq'::regclass);


--
-- TOC entry 2217 (class 2604 OID 28281)
-- Name: mpo_site id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mpo_site ALTER COLUMN id SET DEFAULT nextval('public.mpo_site_id_seq'::regclass);


--
-- TOC entry 2218 (class 2604 OID 28415)
-- Name: opleverrapport_opleverrapport id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.opleverrapport_opleverrapport ALTER COLUMN id SET DEFAULT nextval('public.opleverrapport_opleverrapport_id_seq'::regclass);


--
-- TOC entry 2209 (class 2604 OID 28209)
-- Name: project_klant id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.project_klant ALTER COLUMN id SET DEFAULT nextval('public.project_klant_id_seq'::regclass);


--
-- TOC entry 2210 (class 2604 OID 28217)
-- Name: project_klantmedewerker id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.project_klantmedewerker ALTER COLUMN id SET DEFAULT nextval('public.project_klantmedewerker_id_seq'::regclass);


--
-- TOC entry 2211 (class 2604 OID 28225)
-- Name: project_onderaanemerbedrijf id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.project_onderaanemerbedrijf ALTER COLUMN id SET DEFAULT nextval('public.project_onderaanemerbedrijf_id_seq'::regclass);


--
-- TOC entry 2212 (class 2604 OID 28233)
-- Name: project_project id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.project_project ALTER COLUMN id SET DEFAULT nextval('public.project_project_id_seq'::regclass);


--
-- TOC entry 2213 (class 2604 OID 28246)
-- Name: project_projecticem id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.project_projecticem ALTER COLUMN id SET DEFAULT nextval('public.project_projecticem_id_seq'::regclass);


--
-- TOC entry 2214 (class 2604 OID 28254)
-- Name: project_statusonderaanemer id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.project_statusonderaanemer ALTER COLUMN id SET DEFAULT nextval('public.project_statusonderaanemer_id_seq'::regclass);


--
-- TOC entry 2215 (class 2604 OID 28262)
-- Name: project_vertegenwoordiger_project id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.project_vertegenwoordiger_project ALTER COLUMN id SET DEFAULT nextval('public.project_vertegenwoordiger_project_id_seq'::regclass);


--
-- TOC entry 2219 (class 2604 OID 28522)
-- Name: testrapport_testrapport id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.testrapport_testrapport ALTER COLUMN id SET DEFAULT nextval('public.testrapport_testrapport_id_seq'::regclass);


--
-- TOC entry 2200 (class 2604 OID 28073)
-- Name: users_customuser id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_customuser ALTER COLUMN id SET DEFAULT nextval('public.users_customuser_id_seq'::regclass);


--
-- TOC entry 2205 (class 2604 OID 28128)
-- Name: users_customuser_groups id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_customuser_groups ALTER COLUMN id SET DEFAULT nextval('public.users_customuser_groups_id_seq'::regclass);


--
-- TOC entry 2206 (class 2604 OID 28136)
-- Name: users_customuser_user_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_customuser_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.users_customuser_user_permissions_id_seq'::regclass);


--
-- TOC entry 2204 (class 2604 OID 28115)
-- Name: users_functie id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_functie ALTER COLUMN id SET DEFAULT nextval('public.users_functie_id_seq'::regclass);


--
-- TOC entry 2201 (class 2604 OID 28083)
-- Name: users_klantwoningbouw id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_klantwoningbouw ALTER COLUMN id SET DEFAULT nextval('public.users_klantwoningbouw_id_seq'::regclass);


--
-- TOC entry 2203 (class 2604 OID 28102)
-- Name: users_medewerkerprofile id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_medewerkerprofile ALTER COLUMN id SET DEFAULT nextval('public.users_medewerkerprofile_id_seq'::regclass);


--
-- TOC entry 2202 (class 2604 OID 28091)
-- Name: users_role id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_role ALTER COLUMN id SET DEFAULT nextval('public.users_role_id_seq'::regclass);


--
-- TOC entry 2504 (class 0 OID 28026)
-- Dependencies: 192
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group (id, name) FROM stdin;
1	Admin
\.


--
-- TOC entry 2589 (class 0 OID 0)
-- Dependencies: 191
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- TOC entry 2506 (class 0 OID 28036)
-- Dependencies: 194
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
1	1	29
2	1	32
\.


--
-- TOC entry 2590 (class 0 OID 0)
-- Dependencies: 193
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- TOC entry 2502 (class 0 OID 28018)
-- Dependencies: 190
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add content type	4	add_contenttype
14	Can change content type	4	change_contenttype
15	Can delete content type	4	delete_contenttype
16	Can view content type	4	view_contenttype
17	Can add session	5	add_session
18	Can change session	5	change_session
19	Can delete session	5	delete_session
20	Can view session	5	view_session
21	Can add custom user	6	add_customuser
22	Can change custom user	6	change_customuser
23	Can delete custom user	6	delete_customuser
24	Can view custom user	6	view_customuser
25	Can add klant woningbouw	7	add_klantwoningbouw
26	Can change klant woningbouw	7	change_klantwoningbouw
27	Can delete klant woningbouw	7	delete_klantwoningbouw
28	Can view klant woningbouw	7	view_klantwoningbouw
29	Can add role	8	add_role
30	Can change role	8	change_role
31	Can delete role	8	delete_role
32	Can view role	8	view_role
33	Can add medewerker profile	9	add_medewerkerprofile
34	Can change medewerker profile	9	change_medewerkerprofile
35	Can delete medewerker profile	9	delete_medewerkerprofile
36	Can view medewerker profile	9	view_medewerkerprofile
37	Can add functie	10	add_functie
38	Can change functie	10	change_functie
39	Can delete functie	10	delete_functie
40	Can view functie	10	view_functie
41	Can add klant	11	add_klant
42	Can change klant	11	change_klant
43	Can delete klant	11	delete_klant
44	Can view klant	11	view_klant
45	Can add klant medewerker	12	add_klantmedewerker
46	Can change klant medewerker	12	change_klantmedewerker
47	Can delete klant medewerker	12	delete_klantmedewerker
48	Can view klant medewerker	12	view_klantmedewerker
49	Can add onderaanemerbedrijf	13	add_onderaanemerbedrijf
50	Can change onderaanemerbedrijf	13	change_onderaanemerbedrijf
51	Can delete onderaanemerbedrijf	13	delete_onderaanemerbedrijf
52	Can view onderaanemerbedrijf	13	view_onderaanemerbedrijf
53	Can add project	14	add_project
54	Can change project	14	change_project
55	Can delete project	14	delete_project
56	Can view project	14	view_project
57	Can add project icem	15	add_projecticem
58	Can change project icem	15	change_projecticem
59	Can delete project icem	15	delete_projecticem
60	Can view project icem	15	view_projecticem
61	Can add status onderaanemer	16	add_statusonderaanemer
62	Can change status onderaanemer	16	change_statusonderaanemer
63	Can delete status onderaanemer	16	delete_statusonderaanemer
64	Can view status onderaanemer	16	view_statusonderaanemer
65	Can add vertegenwoordiger_ project	17	add_vertegenwoordiger_project
66	Can change vertegenwoordiger_ project	17	change_vertegenwoordiger_project
67	Can delete vertegenwoordiger_ project	17	delete_vertegenwoordiger_project
68	Can view vertegenwoordiger_ project	17	view_vertegenwoordiger_project
69	Can add bewoners	18	add_bewoners
70	Can change bewoners	18	change_bewoners
71	Can delete bewoners	18	delete_bewoners
72	Can view bewoners	18	view_bewoners
73	Can add site	19	add_site
74	Can change site	19	change_site
75	Can delete site	19	delete_site
76	Can view site	19	view_site
77	Can add bouwkundig	20	add_bouwkundig
78	Can change bouwkundig	20	change_bouwkundig
79	Can delete bouwkundig	20	delete_bouwkundig
80	Can view bouwkundig	20	view_bouwkundig
81	Can add icem	21	add_icem
82	Can change icem	21	change_icem
83	Can delete icem	21	delete_icem
84	Can view icem	21	view_icem
85	Can add boiler	22	add_boiler
86	Can change boiler	22	change_boiler
87	Can delete boiler	22	delete_boiler
88	Can view boiler	22	view_boiler
89	Can add icem debiet	23	add_icemdebiet
90	Can change icem debiet	23	change_icemdebiet
91	Can delete icem debiet	23	delete_icemdebiet
92	Can view icem debiet	23	view_icemdebiet
93	Can add omvormer	24	add_omvormer
94	Can change omvormer	24	change_omvormer
95	Can delete omvormer	24	delete_omvormer
96	Can view omvormer	24	view_omvormer
97	Can add planning	25	add_planning
98	Can change planning	25	change_planning
99	Can delete planning	25	delete_planning
100	Can view planning	25	view_planning
101	Can add productiebon status	26	add_productiebonstatus
102	Can change productiebon status	26	change_productiebonstatus
103	Can delete productiebon status	26	delete_productiebonstatus
104	Can view productiebon status	26	view_productiebonstatus
105	Can add productie exact	27	add_productieexact
106	Can change productie exact	27	change_productieexact
107	Can delete productie exact	27	delete_productieexact
108	Can view productie exact	27	view_productieexact
109	Can add semkast	28	add_semkast
110	Can change semkast	28	change_semkast
111	Can delete semkast	28	delete_semkast
112	Can view semkast	28	view_semkast
113	Can add warmtepomp	29	add_warmtepomp
114	Can change warmtepomp	29	change_warmtepomp
115	Can delete warmtepomp	29	delete_warmtepomp
116	Can view warmtepomp	29	view_warmtepomp
117	Can add wtw	30	add_wtw
118	Can change wtw	30	change_wtw
119	Can delete wtw	30	delete_wtw
120	Can view wtw	30	view_wtw
121	Can add testrapport	31	add_testrapport
122	Can change testrapport	31	change_testrapport
123	Can delete testrapport	31	delete_testrapport
124	Can view testrapport	31	view_testrapport
125	Can add opleverrapport	32	add_opleverrapport
126	Can change opleverrapport	32	change_opleverrapport
127	Can delete opleverrapport	32	delete_opleverrapport
128	Can view opleverrapport	32	view_opleverrapport
\.


--
-- TOC entry 2591 (class 0 OID 0)
-- Dependencies: 189
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 128, true);


--
-- TOC entry 2522 (class 0 OID 28182)
-- Dependencies: 210
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- TOC entry 2592 (class 0 OID 0)
-- Dependencies: 209
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);


--
-- TOC entry 2500 (class 0 OID 28008)
-- Dependencies: 188
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	contenttypes	contenttype
5	sessions	session
6	users	customuser
7	users	klantwoningbouw
8	users	role
9	users	medewerkerprofile
10	users	functie
11	project	klant
12	project	klantmedewerker
13	project	onderaanemerbedrijf
14	project	project
15	project	projecticem
16	project	statusonderaanemer
17	project	vertegenwoordiger_project
18	mpo	bewoners
19	mpo	site
20	mpo	bouwkundig
21	mpo	icem
22	mpo	boiler
23	mpo	icemdebiet
24	mpo	omvormer
25	mpo	planning
26	mpo	productiebonstatus
27	mpo	productieexact
28	mpo	semkast
29	mpo	warmtepomp
30	mpo	wtw
31	testrapport	testrapport
32	opleverrapport	opleverrapport
\.


--
-- TOC entry 2593 (class 0 OID 0)
-- Dependencies: 187
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 32, true);


--
-- TOC entry 2498 (class 0 OID 27997)
-- Dependencies: 186
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2023-04-20 14:55:08.317964+02
2	contenttypes	0002_remove_content_type_name	2023-04-20 14:55:08.349395+02
3	auth	0001_initial	2023-04-20 14:55:08.458621+02
4	auth	0002_alter_permission_name_max_length	2023-04-20 14:55:08.467597+02
5	auth	0003_alter_user_email_max_length	2023-04-20 14:55:08.483286+02
6	auth	0004_alter_user_username_opts	2023-04-20 14:55:08.503562+02
7	auth	0005_alter_user_last_login_null	2023-04-20 14:55:08.516525+02
8	auth	0006_require_contenttypes_0002	2023-04-20 14:55:08.520512+02
9	auth	0007_alter_validators_add_error_messages	2023-04-20 14:55:08.532481+02
10	auth	0008_alter_user_username_max_length	2023-04-20 14:55:08.546319+02
11	auth	0009_alter_user_last_name_max_length	2023-04-20 14:55:08.562283+02
12	auth	0010_alter_group_name_max_length	2023-04-20 14:55:08.580082+02
13	auth	0011_update_proxy_permissions	2023-04-20 14:55:08.594955+02
14	auth	0012_alter_user_first_name_max_length	2023-04-20 14:55:08.613075+02
15	users	0001_initial	2023-04-20 14:55:08.829355+02
16	admin	0001_initial	2023-04-20 14:55:08.901711+02
17	admin	0002_logentry_remove_auto_add	2023-04-20 14:55:08.927636+02
18	admin	0003_logentry_add_action_flag_choices	2023-04-20 14:55:08.953294+02
19	project	0001_initial	2023-04-20 14:55:09.066524+02
20	mpo	0001_initial	2023-04-20 14:55:09.15186+02
21	mpo	0002_initial	2023-04-20 14:55:09.385865+02
22	opleverrapport	0001_initial	2023-04-20 14:55:09.408381+02
23	opleverrapport	0002_initial	2023-04-20 14:55:09.525204+02
24	project	0002_initial	2023-04-20 14:55:09.847949+02
25	sessions	0001_initial	2023-04-20 14:55:09.876504+02
26	testrapport	0001_initial	2023-04-20 14:55:09.9124+02
27	testrapport	0002_initial	2023-04-20 14:55:10.07764+02
\.


--
-- TOC entry 2594 (class 0 OID 0)
-- Dependencies: 185
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 27, true);


--
-- TOC entry 2554 (class 0 OID 28507)
-- Dependencies: 242
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
s2h3mgy6onl3izcg7uto9ifec4xcbjei	.eJxVjMEKwyAQRP_FcxGtqa499p5vkHVXa9piICan0n-vgRxaGBiYNzNvEXBbS9haWsLE4iq0OP1mEemZ6g74gfU-S5rrukxR7hV50CbHmdPrdnT_Dgq20teKwHsgjT4667oZTiahIbYXxUCJo9FdJpMF5dh65XL0oN1wBjVk8fkC6NI3sw:1pqCKw:_jq8gKxOtwCMKg-ZLbhc6nsRW4XYrjO2HIn9FWskX8U	2023-05-06 14:27:30.374337+02
zc4s90jiutr0ve2ga0ikgltle8r5r9fy	.eJxVjMEKwyAQRP_FcxGtqa499p5vkHVXa9piICan0n-vgRxaGBiYNzNvEXBbS9haWsLE4iq0OP1mEemZ6g74gfU-S5rrukxR7hV50CbHmdPrdnT_Dgq20teKwHsgjT4667oZTiahIbYXxUCJo9FdJpMF5dh65XL0oN1wBjVk8fkC6NI3sw:1ppUrE:BIbEzkK3bZjOHNCLVZMskf66WFX9y1mSBIzu78GcXuY	2023-05-04 16:01:56.089211+02
18yrc0fpqyo1cqnfrnu2vji22djspeaj	.eJxVjMEKwyAQRP_FcxGtqa499p5vkHVXa9piICan0n-vgRxaGBiYNzNvEXBbS9haWsLE4iq0OP1mEemZ6g74gfU-S5rrukxR7hV50CbHmdPrdnT_Dgq20teKwHsgjT4667oZTiahIbYXxUCJo9FdJpMF5dh65XL0oN1wBjVk8fkC6NI3sw:1ppUrE:BIbEzkK3bZjOHNCLVZMskf66WFX9y1mSBIzu78GcXuY	2023-05-04 16:01:56.089211+02
0ecu83hant72ahocisjdtzqbpnct255l	.eJxVjMEKwyAQRP_FcxGtqa499p5vkHVXa9piICan0n-vgRxaGBiYNzNvEXBbS9haWsLE4iq0OP1mEemZ6g74gfU-S5rrukxR7hV50CbHmdPrdnT_Dgq20teKwHsgjT4667oZTiahIbYXxUCJo9FdJpMF5dh65XL0oN1wBjVk8fkC6NI3sw:1prCaw:l0RUwM1wCvVWAvbo5c7DyNqJGIlDfEwiU_KaUXfHuLs	2023-05-09 08:56:10.536585+02
3n2ui11naoe72z2y2v0yncof68f45zz5	.eJxVjMEKwyAQRP_FcxGtqa499p5vkHVXa9piICan0n-vgRxaGBiYNzNvEXBbS9haWsLE4iq0OP1mEemZ6g74gfU-S5rrukxR7hV50CbHmdPrdnT_Dgq20teKwHsgjT4667oZTiahIbYXxUCJo9FdJpMF5dh65XL0oN1wBjVk8fkC6NI3sw:1prCaw:l0RUwM1wCvVWAvbo5c7DyNqJGIlDfEwiU_KaUXfHuLs	2023-05-09 08:56:10.539579+02
y8elnbeq8xwoxkhxfgkmfqacyquujzay	.eJxVjMsOwiAURP-FtSFcHkVcuvcbyAUuUjWQlHZl_Hdp0oXuJnPOzJt53Nbit06LnxO7sDM7_XYB45PqDtID673x2Oq6zIHvCj9o57eW6HU93L-Dgr2Mtc6WApCyzorknIMcSUZhkooECWBCY_OkJdAIZDISCBkyKZJy-Jp9vvLGOD4:1prEgY:WH-mRO_VUC6n69S4tEMCv8MVCVNqBevWlgI1TSEbI-o	2023-05-09 11:10:06.421606+02
ssa0tueaff82namghboikmdnkc2xyhcr	.eJxVjMsOwiAQRf-FtSEUyqMu3fsNZIYZpGogKe3K-O_apAvd3nPOfYkI21ri1nmJM4mz8OL0uyGkB9cd0B3qrcnU6rrMKHdFHrTLayN-Xg7376BAL99a56QsjU6Z4FllRuXHbJEBEhkE0G6izH4KWTsKaANqw24YtEbrc7Li_QEFLziX:1prZmE:xciKr6rM1ps51vbDl8Rf8EpwibFSp0gd-d1ZUDjErbw	2023-05-10 09:41:22.91617+02
pxnkzbzbbjjyji3waenl476ttio8ulc0	.eJxVjMsOwiAURP-FtSFcHkVcuvcbyAUuUjWQlHZl_Hdp0oXuJnPOzJt53Nbit06LnxO7sDM7_XYB45PqDtID673x2Oq6zIHvCj9o57eW6HU93L-Dgr2Mtc6WApCyzorknIMcSUZhkooECWBCY_OkJdAIZDISCBkyKZJy-Jp9vvLGOD4:1prZmq:gpL0llJBjF2ykd7NeqsjVswHCflQcX4MGysPdmOpwW4	2023-05-10 09:42:00.36906+02
tgmv9ftodlfbtm3t7pcxxoj5o5qzhi93	.eJxVjMsOwiAURP-FtSFcHkVcuvcbyAUuUjWQlHZl_Hdp0oXuJnPOzJt53Nbit06LnxO7sDM7_XYB45PqDtID673x2Oq6zIHvCj9o57eW6HU93L-Dgr2Mtc6WApCyzorknIMcSUZhkooECWBCY_OkJdAIZDISCBkyKZJy-Jp9vvLGOD4:1psAe6:tGsRrYObJdSQyRQefaAnfOfTDue5yGWpd36HVSRs3LQ	2023-05-12 01:03:26.480276+02
czg56q1yigxc6qe5gn28ce74zy3v6hfx	.eJxVjMsOwiAURP-FtSFcHkVcuvcbyAUuUjWQlHZl_Hdp0oXuJnPOzJt53Nbit06LnxO7sDM7_XYB45PqDtID673x2Oq6zIHvCj9o57eW6HU93L-Dgr2Mtc6WApCyzorknIMcSUZhkooECWBCY_OkJdAIZDISCBkyKZJy-Jp9vvLGOD4:1psIvx:EksIeOzj6NEMTUcTPHavS5y1V8g_uvdqCWJgRkwkxgQ	2023-05-12 09:54:25.583984+02
adyvl2x19a0ou3cgy7tjaeio27xkppsq	.eJxVjMsOwiAURP-FtSFcHkVcuvcbyAUuUjWQlHZl_Hdp0oXuJnPOzJt53Nbit06LnxO7sDM7_XYB45PqDtID673x2Oq6zIHvCj9o57eW6HU93L-Dgr2Mtc6WApCyzorknIMcSUZhkooECWBCY_OkJdAIZDISCBkyKZJy-Jp9vvLGOD4:1psS4I:-OBaMuSLn8aNVMU4iYwZRrclD6NDuS1XSzmYMhHt5rs	2023-05-12 19:39:38.061655+02
xoym6i6hbn4h1931c1rnvvjqjckmbgp3	.eJxVjMsOwiAQRf-FtSEUyqMu3fsNZIYZpGogKe3K-O_apAvd3nPOfYkI21ri1nmJM4mz8OL0uyGkB9cd0B3qrcnU6rrMKHdFHrTLayN-Xg7376BAL99a56QsjU6Z4FllRuXHbJEBEhkE0G6izH4KWTsKaANqw24YtEbrc7Li_QEFLziX:1pqAeg:0gi3NAsCce_W1ls7v2xXDVs4IVRxyc0NWG8dn4qfgPE	2023-05-06 12:39:46.608833+02
4k3p5g3yqhnwmy48x3rj6vo6gtdscinh	.eJxVjMsOwiAQRf-FtSE8SgWX7vsNZGYYpGogKe3K-O_apAvd3nPOfYkI21ri1nmJcxIXocXpd0OgB9cdpDvUW5PU6rrMKHdFHrTLqSV-Xg_376BAL99asVfaMuDIzgQ3BO184EwDgnFMCQOZkMiPilD5rAAGstYoZzKac0bx_gDqyjhU:1ptB5J:esuuGmxD3coJFH_5Vd5s2pNZzvqBy7-N7E6_b96W7P0	2023-05-14 19:43:41.330974+02
fvf9hjiskn9o8qkybl4qq1b418ljx9te	.eJxVjM0OwiAQhN-FsyEUKT8evfsMZFl2pWogKe3J-O62SQ86x_m-mbeIsC4lrp3mOGVxEV6cfrsE-KS6g_yAem8SW13mKcldkQft8tYyva6H-3dQoJdtHYKFhAN7tGx4BEB0nA0Csw426TNtMWSDJ1RajW5AFcgHNmA0OxKfLyb4OUQ:1ptCMg:wcsEMyKw9oYUdANuRtXZv0PUB5IpQcYtPcThnt774xk	2023-05-14 21:05:42.186826+02
\.


--
-- TOC entry 2538 (class 0 OID 28268)
-- Dependencies: 226
-- Data for Name: mpo_bewoners; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.mpo_bewoners (id, aanhef_bewoner, achternaam_bewoner, voorletters_bewoner, phone_bewoner, tussenvoegsels_bewoner, email_bewoner, site_id) FROM stdin;
5	\N	\N	\N	\N	\N	\N	1
4	\N	\N	\N	\N	\N	\N	2
3	\N	\N	\N	\N	\N	\N	3
2	\N	\N	\N	\N	\N	\N	4
1	\N	\N	\N	\N	\N	\N	5
121	\N	\N	\N	\N	\N	\N	40
120	\N	\N	\N	\N	\N	\N	41
119	\N	\N	\N	\N	\N	\N	42
118	\N	\N	\N	\N	\N	\N	43
117	\N	\N	\N	\N	\N	\N	44
116	\N	\N	\N	\N	\N	\N	45
115	\N	\N	\N	\N	\N	\N	46
114	\N	\N	\N	\N	\N	\N	47
113	\N	\N	\N	\N	\N	\N	48
112	\N	\N	\N	\N	\N	\N	49
111	\N	\N	\N	\N	\N	\N	50
110	\N	\N	\N	\N	\N	\N	51
109	\N	\N	\N	\N	\N	\N	52
108	\N	\N	\N	\N	\N	\N	53
107	\N	\N	\N	\N	\N	\N	54
106	\N	\N	\N	\N	\N	\N	55
105	\N	\N	\N	\N	\N	\N	56
104	\N	\N	\N	\N	\N	\N	57
103	\N	\N	\N	\N	\N	\N	58
102	\N	\N	\N	\N	\N	\N	59
101	\N	\N	\N	\N	\N	\N	60
100	\N	\N	\N	\N	\N	\N	61
99	\N	\N	\N	\N	\N	\N	62
98	\N	\N	\N	\N	\N	\N	63
97	\N	\N	\N	\N	\N	\N	64
96	\N	\N	\N	\N	\N	\N	65
95	\N	\N	\N	\N	\N	\N	66
94	\N	\N	\N	\N	\N	\N	67
93	\N	\N	\N	\N	\N	\N	68
92	\N	\N	\N	\N	\N	\N	69
91	\N	\N	\N	\N	\N	\N	70
90	\N	\N	\N	\N	\N	\N	71
89	\N	\N	\N	\N	\N	\N	72
88	\N	\N	\N	\N	\N	\N	73
87	\N	\N	\N	\N	\N	\N	74
86	\N	\N	\N	\N	\N	\N	75
85	\N	\N	\N	\N	\N	\N	76
84	\N	\N	\N	\N	\N	\N	77
83	\N	\N	\N	\N	\N	\N	78
82	\N	\N	\N	\N	\N	\N	79
81	\N	\N	\N	\N	\N	\N	80
80	\N	\N	\N	\N	\N	\N	81
79	\N	\N	\N	\N	\N	\N	82
78	\N	\N	\N	\N	\N	\N	83
77	\N	\N	\N	\N	\N	\N	84
76	\N	\N	\N	\N	\N	\N	85
75	\N	\N	\N	\N	\N	\N	86
74	\N	\N	\N	\N	\N	\N	87
73	\N	\N	\N	\N	\N	\N	88
72	\N	\N	\N	\N	\N	\N	89
71	\N	\N	\N	\N	\N	\N	90
70	\N	\N	\N	\N	\N	\N	91
69	\N	\N	\N	\N	\N	\N	92
68	\N	\N	\N	\N	\N	\N	93
155	\N	\N	\N	\N	\N	\N	6
154	\N	\N	\N	\N	\N	\N	7
153	\N	\N	\N	\N	\N	\N	8
152	\N	\N	\N	\N	\N	\N	9
151	\N	\N	\N	\N	\N	\N	10
150	\N	\N	\N	\N	\N	\N	11
149	\N	\N	\N	\N	\N	\N	12
148	\N	\N	\N	\N	\N	\N	13
147	\N	\N	\N	\N	\N	\N	14
146	\N	\N	\N	\N	\N	\N	15
145	\N	\N	\N	\N	\N	\N	16
144	\N	\N	\N	\N	\N	\N	17
143	\N	\N	\N	\N	\N	\N	18
142	\N	\N	\N	\N	\N	\N	19
141	\N	\N	\N	\N	\N	\N	20
140	\N	\N	\N	\N	\N	\N	21
139	\N	\N	\N	\N	\N	\N	22
138	\N	\N	\N	\N	\N	\N	23
137	\N	\N	\N	\N	\N	\N	24
136	\N	\N	\N	\N	\N	\N	25
135	\N	\N	\N	\N	\N	\N	26
134	\N	\N	\N	\N	\N	\N	27
133	\N	\N	\N	\N	\N	\N	28
132	\N	\N	\N	\N	\N	\N	29
131	\N	\N	\N	\N	\N	\N	30
130	\N	\N	\N	\N	\N	\N	31
129	\N	\N	\N	\N	\N	\N	32
128	\N	\N	\N	\N	\N	\N	33
127	\N	\N	\N	\N	\N	\N	34
126	\N	\N	\N	\N	\N	\N	35
125	\N	\N	\N	\N	\N	\N	36
124	\N	\N	\N	\N	\N	\N	37
123	\N	\N	\N	\N	\N	\N	38
122	\N	\N	\N	\N	\N	\N	39
67	\N	\N	\N	\N	\N	\N	94
66	\N	\N	\N	\N	\N	\N	95
65	\N	\N	\N	\N	\N	\N	96
64	\N	\N	\N	\N	\N	\N	97
63	\N	\N	\N	\N	\N	\N	98
62	\N	\N	\N	\N	\N	\N	99
61	\N	\N	\N	\N	\N	\N	100
60	\N	\N	\N	\N	\N	\N	101
59	\N	\N	\N	\N	\N	\N	102
58	\N	\N	\N	\N	\N	\N	103
57	\N	\N	\N	\N	\N	\N	104
56	\N	\N	\N	\N	\N	\N	105
55	\N	\N	\N	\N	\N	\N	106
54	\N	\N	\N	\N	\N	\N	107
53	\N	\N	\N	\N	\N	\N	108
52	\N	\N	\N	\N	\N	\N	109
51	\N	\N	\N	\N	\N	\N	110
50	\N	\N	\N	\N	\N	\N	111
49	\N	\N	\N	\N	\N	\N	112
48	\N	\N	\N	\N	\N	\N	113
47	\N	\N	\N	\N	\N	\N	114
46	\N	\N	\N	\N	\N	\N	115
45	\N	\N	\N	\N	\N	\N	116
44	\N	\N	\N	\N	\N	\N	117
43	\N	\N	\N	\N	\N	\N	118
42	\N	\N	\N	\N	\N	\N	119
41	\N	\N	\N	\N	\N	\N	120
40	\N	\N	\N	\N	\N	\N	121
39	\N	\N	\N	\N	\N	\N	122
38	\N	\N	\N	\N	\N	\N	123
37	\N	\N	\N	\N	\N	\N	124
36	\N	\N	\N	\N	\N	\N	125
35	\N	\N	\N	\N	\N	\N	126
34	\N	\N	\N	\N	\N	\N	127
33	\N	\N	\N	\N	\N	\N	128
32	\N	\N	\N	\N	\N	\N	129
31	\N	\N	\N	\N	\N	\N	130
30	\N	\N	\N	\N	\N	\N	131
29	\N	\N	\N	\N	\N	\N	132
28	\N	\N	\N	\N	\N	\N	133
27	\N	\N	\N	\N	\N	\N	134
26	\N	\N	\N	\N	\N	\N	135
25	\N	\N	\N	\N	\N	\N	136
24	\N	\N	\N	\N	\N	\N	137
23	\N	\N	\N	\N	\N	\N	138
22	\N	\N	\N	\N	\N	\N	139
21	\N	\N	\N	\N	\N	\N	140
20	\N	\N	\N	\N	\N	\N	141
19	\N	\N	\N	\N	\N	\N	142
18	\N	\N	\N	\N	\N	\N	143
17	\N	\N	\N	\N	\N	\N	144
16	\N	\N	\N	\N	\N	\N	145
15	\N	\N	\N	\N	\N	\N	146
14	\N	\N	\N	\N	\N	\N	147
13	\N	\N	\N	\N	\N	\N	148
12	\N	\N	\N	\N	\N	\N	149
11	\N	\N	\N	\N	\N	\N	150
10	\N	\N	\N	\N	\N	\N	151
9	\N	\N	\N	\N	\N	\N	152
8	\N	\N	\N	\N	\N	\N	153
7	\N	\N	\N	\N	\N	\N	154
6	\N	\N	\N	\N	\N	\N	155
\.


--
-- TOC entry 2595 (class 0 OID 0)
-- Dependencies: 225
-- Name: mpo_bewoners_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.mpo_bewoners_id_seq', 155, true);


--
-- TOC entry 2543 (class 0 OID 28318)
-- Dependencies: 231
-- Data for Name: mpo_boiler; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.mpo_boiler (inhoud, icem_id) FROM stdin;
\N	6
\N	7
\N	8
\N	9
\N	10
\N	11
\N	12
\N	13
\N	14
\N	15
\N	16
\N	17
\N	18
\N	19
\N	20
\N	21
\N	22
\N	23
\N	24
\N	25
\N	26
\N	27
\N	28
\N	29
\N	30
\N	1
\N	2
\N	3
\N	4
\N	5
\N	31
\N	32
\N	33
\N	34
\N	35
\N	36
\N	37
\N	38
\N	39
\N	40
\N	41
\N	42
\N	43
\N	44
\N	45
\N	46
\N	47
\N	48
\N	49
\N	50
\N	51
\N	52
\N	53
\N	54
\N	55
\N	56
\N	57
\N	58
\N	59
\N	60
\N	61
\N	62
\N	63
\N	64
\N	65
\N	66
\N	67
\N	68
\N	69
\N	70
\N	71
\N	72
\N	73
\N	74
\N	75
\N	76
\N	77
\N	78
\N	79
\N	80
\N	81
\N	82
\N	83
\N	84
\N	85
\N	86
\N	87
\N	88
\N	89
\N	90
\N	91
\N	92
\N	93
\N	94
\N	95
\N	96
\N	97
\N	98
\N	99
\N	100
\N	101
\N	102
\N	103
\N	104
\N	105
\N	106
\N	107
\N	108
\N	109
\N	110
\N	111
\N	112
\N	113
\N	114
\N	115
\N	116
\N	117
\N	118
\N	119
\N	120
\N	121
\N	122
\N	123
\N	124
\N	125
\N	126
\N	127
\N	128
\N	129
\N	130
\N	131
\N	132
\N	133
\N	134
\N	135
\N	136
\N	137
\N	138
\N	139
\N	140
\N	141
\N	142
\N	143
\N	144
\N	145
\N	146
\N	147
\N	148
\N	149
\N	150
\N	151
\N	152
\N	153
\N	154
\N	155
\.


--
-- TOC entry 2541 (class 0 OID 28287)
-- Dependencies: 229
-- Data for Name: mpo_bouwkundig; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.mpo_bouwkundig ("nokHoogte", "nokDiepte", "typeDak", "positieBuitendeel", site_id) FROM stdin;
\N	\N	\N	\N	6
\N	\N	\N	\N	7
\N	\N	\N	\N	8
\N	\N	\N	\N	9
\N	\N	\N	\N	10
\N	\N	\N	\N	11
\N	\N	\N	\N	12
\N	\N	\N	\N	13
\N	\N	\N	\N	14
\N	\N	\N	\N	15
\N	\N	\N	\N	16
\N	\N	\N	\N	17
\N	\N	\N	\N	18
\N	\N	\N	\N	19
\N	\N	\N	\N	20
\N	\N	\N	\N	21
\N	\N	\N	\N	22
\N	\N	\N	\N	23
\N	\N	\N	\N	24
\N	\N	\N	\N	25
\N	\N	\N	\N	26
\N	\N	\N	\N	27
\N	\N	\N	\N	28
\N	\N	\N	\N	29
\N	\N	\N	\N	30
\N	\N	\N	\N	1
\N	\N	\N	\N	2
\N	\N	\N	\N	3
\N	\N	\N	\N	4
\N	\N	\N	\N	5
\N	\N	\N	\N	31
\N	\N	\N	\N	32
\N	\N	\N	\N	33
\N	\N	\N	\N	34
\N	\N	\N	\N	35
\N	\N	\N	\N	36
\N	\N	\N	\N	37
\N	\N	\N	\N	38
\N	\N	\N	\N	39
\N	\N	\N	\N	40
\N	\N	\N	\N	41
\N	\N	\N	\N	42
\N	\N	\N	\N	43
\N	\N	\N	\N	44
\N	\N	\N	\N	45
\N	\N	\N	\N	46
\N	\N	\N	\N	47
\N	\N	\N	\N	48
\N	\N	\N	\N	49
\N	\N	\N	\N	50
\N	\N	\N	\N	51
\N	\N	\N	\N	52
\N	\N	\N	\N	53
\N	\N	\N	\N	54
\N	\N	\N	\N	55
\N	\N	\N	\N	56
\N	\N	\N	\N	57
\N	\N	\N	\N	58
\N	\N	\N	\N	59
\N	\N	\N	\N	60
\N	\N	\N	\N	61
\N	\N	\N	\N	62
\N	\N	\N	\N	63
\N	\N	\N	\N	64
\N	\N	\N	\N	65
\N	\N	\N	\N	66
\N	\N	\N	\N	67
\N	\N	\N	\N	68
\N	\N	\N	\N	69
\N	\N	\N	\N	70
\N	\N	\N	\N	71
\N	\N	\N	\N	72
\N	\N	\N	\N	73
\N	\N	\N	\N	74
\N	\N	\N	\N	75
\N	\N	\N	\N	76
\N	\N	\N	\N	77
\N	\N	\N	\N	78
\N	\N	\N	\N	79
\N	\N	\N	\N	80
\N	\N	\N	\N	81
\N	\N	\N	\N	82
\N	\N	\N	\N	83
\N	\N	\N	\N	84
\N	\N	\N	\N	85
\N	\N	\N	\N	86
\N	\N	\N	\N	87
\N	\N	\N	\N	88
\N	\N	\N	\N	89
\N	\N	\N	\N	90
\N	\N	\N	\N	91
\N	\N	\N	\N	92
\N	\N	\N	\N	93
\N	\N	\N	\N	94
\N	\N	\N	\N	95
\N	\N	\N	\N	96
\N	\N	\N	\N	97
\N	\N	\N	\N	98
\N	\N	\N	\N	99
\N	\N	\N	\N	100
\N	\N	\N	\N	101
\N	\N	\N	\N	102
\N	\N	\N	\N	103
\N	\N	\N	\N	104
\N	\N	\N	\N	105
\N	\N	\N	\N	106
\N	\N	\N	\N	107
\N	\N	\N	\N	108
\N	\N	\N	\N	109
\N	\N	\N	\N	110
\N	\N	\N	\N	111
\N	\N	\N	\N	112
\N	\N	\N	\N	113
\N	\N	\N	\N	114
\N	\N	\N	\N	115
\N	\N	\N	\N	116
\N	\N	\N	\N	117
\N	\N	\N	\N	118
\N	\N	\N	\N	119
\N	\N	\N	\N	120
\N	\N	\N	\N	121
\N	\N	\N	\N	122
\N	\N	\N	\N	123
\N	\N	\N	\N	124
\N	\N	\N	\N	125
\N	\N	\N	\N	126
\N	\N	\N	\N	127
\N	\N	\N	\N	128
\N	\N	\N	\N	129
\N	\N	\N	\N	130
\N	\N	\N	\N	131
\N	\N	\N	\N	132
\N	\N	\N	\N	133
\N	\N	\N	\N	134
\N	\N	\N	\N	135
\N	\N	\N	\N	136
\N	\N	\N	\N	137
\N	\N	\N	\N	138
\N	\N	\N	\N	139
\N	\N	\N	\N	140
\N	\N	\N	\N	141
\N	\N	\N	\N	142
\N	\N	\N	\N	143
\N	\N	\N	\N	144
\N	\N	\N	\N	145
\N	\N	\N	\N	146
\N	\N	\N	\N	147
\N	\N	\N	\N	148
\N	\N	\N	\N	149
\N	\N	\N	\N	150
\N	\N	\N	\N	151
\N	\N	\N	\N	152
\N	\N	\N	\N	153
\N	\N	\N	\N	154
\N	\N	\N	\N	155
\.


--
-- TOC entry 2542 (class 0 OID 28292)
-- Dependencies: 230
-- Data for Name: mpo_icem; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.mpo_icem (site_id, "icemType", "energieModule", "positieIcem", aansluitingkanalen, kwh_meter, "sensoringOptie", type_prestatie, koeling, "positieWPmodule") FROM stdin;
115	\N	\N	\N	\N	\N	\N	\N	\N	\N
116	\N	\N	\N	\N	\N	\N	\N	\N	\N
117	\N	\N	\N	\N	\N	\N	\N	\N	\N
118	\N	\N	\N	\N	\N	\N	\N	\N	\N
119	\N	\N	\N	\N	\N	\N	\N	\N	\N
120	\N	\N	\N	\N	\N	\N	\N	\N	\N
121	\N	\N	\N	\N	\N	\N	\N	\N	\N
122	\N	\N	\N	\N	\N	\N	\N	\N	\N
123	\N	\N	\N	\N	\N	\N	\N	\N	\N
124	\N	\N	\N	\N	\N	\N	\N	\N	\N
125	\N	\N	\N	\N	\N	\N	\N	\N	\N
126	\N	\N	\N	\N	\N	\N	\N	\N	\N
127	\N	\N	\N	\N	\N	\N	\N	\N	\N
128	\N	\N	\N	\N	\N	\N	\N	\N	\N
129	\N	\N	\N	\N	\N	\N	\N	\N	\N
130	\N	\N	\N	\N	\N	\N	\N	\N	\N
131	\N	\N	\N	\N	\N	\N	\N	\N	\N
132	\N	\N	\N	\N	\N	\N	\N	\N	\N
133	\N	\N	\N	\N	\N	\N	\N	\N	\N
134	\N	\N	\N	\N	\N	\N	\N	\N	\N
135	\N	\N	\N	\N	\N	\N	\N	\N	\N
136	\N	\N	\N	\N	\N	\N	\N	\N	\N
137	\N	\N	\N	\N	\N	\N	\N	\N	\N
138	\N	\N	\N	\N	\N	\N	\N	\N	\N
139	\N	\N	\N	\N	\N	\N	\N	\N	\N
1	i	6007	Links	\N	\N	\N	\N	\N	- Kies optie -
2	i	7098	Rechts	\N	\N	\N	\N	\N	\N
3	a	\N	\N	\N	\N	\N	\N	\N	\N
4	a	\N	\N	\N	\N	\N	\N	\N	\N
5	p	\N	\N	\N	\N	\N	\N	\N	\N
13	\N	\N	\N	\N	\N	\N	\N	\N	\N
14	\N	\N	\N	\N	\N	\N	\N	\N	\N
15	\N	\N	\N	\N	\N	\N	\N	\N	\N
16	\N	\N	\N	\N	\N	\N	\N	\N	\N
17	\N	\N	\N	\N	\N	\N	\N	\N	\N
18	\N	\N	\N	\N	\N	\N	\N	\N	\N
19	\N	\N	\N	\N	\N	\N	\N	\N	\N
20	\N	\N	\N	\N	\N	\N	\N	\N	\N
21	\N	\N	\N	\N	\N	\N	\N	\N	\N
22	\N	\N	\N	\N	\N	\N	\N	\N	\N
23	\N	\N	\N	\N	\N	\N	\N	\N	\N
24	\N	\N	\N	\N	\N	\N	\N	\N	\N
25	\N	\N	\N	\N	\N	\N	\N	\N	\N
26	\N	\N	\N	\N	\N	\N	\N	\N	\N
27	\N	\N	\N	\N	\N	\N	\N	\N	\N
28	\N	\N	\N	\N	\N	\N	\N	\N	\N
29	\N	\N	\N	\N	\N	\N	\N	\N	\N
30	\N	\N	\N	\N	\N	\N	\N	\N	\N
31	\N	\N	\N	\N	\N	\N	\N	\N	\N
32	\N	\N	\N	\N	\N	\N	\N	\N	\N
33	\N	\N	\N	\N	\N	\N	\N	\N	\N
34	i		\N	\N	\N	\N	\N	\N	\N
35	a	\N	\N	\N	\N	\N	\N	\N	\N
36	a	\N	\N	\N	\N	\N	\N	\N	\N
37	p	\N	\N	\N	\N	\N	\N	\N	\N
38	\N	\N	\N	\N	\N	\N	\N	\N	\N
39	\N	\N	\N	\N	\N	\N	\N	\N	\N
140	\N	\N	\N	\N	\N	\N	\N	\N	\N
141	\N	\N	\N	\N	\N	\N	\N	\N	\N
142	\N	\N	\N	\N	\N	\N	\N	\N	\N
143	\N	\N	\N	\N	\N	\N	\N	\N	\N
144	\N	\N	\N	\N	\N	\N	\N	\N	\N
145	\N	\N	\N	\N	\N	\N	\N	\N	\N
146	\N	\N	\N	\N	\N	\N	\N	\N	\N
147	\N	\N	\N	\N	\N	\N	\N	\N	\N
148	\N	\N	\N	\N	\N	\N	\N	\N	\N
149	\N	\N	\N	\N	\N	\N	\N	\N	\N
40	\N	\N	\N	\N	\N	\N	\N	\N	\N
41	\N	\N	\N	\N	\N	\N	\N	\N	\N
42	\N	\N	\N	\N	\N	\N	\N	\N	\N
43	\N	\N	\N	\N	\N	\N	\N	\N	\N
44	\N	\N	\N	\N	\N	\N	\N	\N	\N
45	\N	\N	\N	\N	\N	\N	\N	\N	\N
46	\N	\N	\N	\N	\N	\N	\N	\N	\N
47	\N	\N	\N	\N	\N	\N	\N	\N	\N
110	\N	\N	\N	\N	\N	\N	\N	\N	\N
111	\N	\N	\N	\N	\N	\N	\N	\N	\N
112	\N	\N	\N	\N	\N	\N	\N	\N	\N
113	\N	\N	\N	\N	\N	\N	\N	\N	\N
114	\N	\N	\N	\N	\N	\N	\N	\N	\N
150	\N	\N	\N	\N	\N	\N	\N	\N	\N
151	\N	\N	\N	\N	\N	\N	\N	\N	\N
152	\N	\N	\N	\N	\N	\N	\N	\N	\N
153	\N	\N	\N	\N	\N	\N	\N	\N	\N
154	\N	\N	\N	\N	\N	\N	\N	\N	\N
155	\N	\N	\N	\N	\N	\N	\N	\N	\N
6	i	\N	\N	\N	\N	\N	\N	\N	\N
7	p	\N	\N	\N	\N	\N	\N	\N	\N
8	e	\N	\N	\N	\N	\N	\N	\N	\N
9	f	\N	\N	\N	\N	\N	\N	\N	\N
10	f	\N	\N	\N	\N	\N	\N	\N	\N
11	p	\N	\N	\N	\N	\N	\N	\N	\N
12	\N	\N	\N	\N	\N	\N	\N	\N	\N
48	\N	\N	\N	\N	\N	\N	\N	\N	\N
49	\N	\N	\N	\N	\N	\N	\N	\N	\N
50	\N	\N	\N	\N	\N	\N	\N	\N	\N
51	\N	\N	\N	\N	\N	\N	\N	\N	\N
52	\N	\N	\N	\N	\N	\N	\N	\N	\N
53	\N	\N	\N	\N	\N	\N	\N	\N	\N
54	\N	\N	\N	\N	\N	\N	\N	\N	\N
55	\N	\N	\N	\N	\N	\N	\N	\N	\N
56	\N	\N	\N	\N	\N	\N	\N	\N	\N
57	\N	\N	\N	\N	\N	\N	\N	\N	\N
58	\N	\N	\N	\N	\N	\N	\N	\N	\N
59	\N	\N	\N	\N	\N	\N	\N	\N	\N
60	\N	\N	\N	\N	\N	\N	\N	\N	\N
61	\N	\N	\N	\N	\N	\N	\N	\N	\N
62	\N	\N	\N	\N	\N	\N	\N	\N	\N
63	\N	\N	\N	\N	\N	\N	\N	\N	\N
64	\N	\N	\N	\N	\N	\N	\N	\N	\N
65	\N	\N	\N	\N	\N	\N	\N	\N	\N
66	\N	\N	\N	\N	\N	\N	\N	\N	\N
67	\N	\N	\N	\N	\N	\N	\N	\N	\N
68	\N	\N	\N	\N	\N	\N	\N	\N	\N
69	\N	\N	\N	\N	\N	\N	\N	\N	\N
70	\N	\N	\N	\N	\N	\N	\N	\N	\N
71	\N	\N	\N	\N	\N	\N	\N	\N	\N
72	\N	\N	\N	\N	\N	\N	\N	\N	\N
73	\N	\N	\N	\N	\N	\N	\N	\N	\N
74	\N	\N	\N	\N	\N	\N	\N	\N	\N
75	\N	\N	\N	\N	\N	\N	\N	\N	\N
76	\N	\N	\N	\N	\N	\N	\N	\N	\N
77	\N	\N	\N	\N	\N	\N	\N	\N	\N
78	\N	\N	\N	\N	\N	\N	\N	\N	\N
79	\N	\N	\N	\N	\N	\N	\N	\N	\N
80	\N	\N	\N	\N	\N	\N	\N	\N	\N
81	\N	\N	\N	\N	\N	\N	\N	\N	\N
82	\N	\N	\N	\N	\N	\N	\N	\N	\N
83	\N	\N	\N	\N	\N	\N	\N	\N	\N
84	\N	\N	\N	\N	\N	\N	\N	\N	\N
85	\N	\N	\N	\N	\N	\N	\N	\N	\N
86	\N	\N	\N	\N	\N	\N	\N	\N	\N
87	\N	\N	\N	\N	\N	\N	\N	\N	\N
88	\N	\N	\N	\N	\N	\N	\N	\N	\N
89	\N	\N	\N	\N	\N	\N	\N	\N	\N
90	\N	\N	\N	\N	\N	\N	\N	\N	\N
91	\N	\N	\N	\N	\N	\N	\N	\N	\N
92	\N	\N	\N	\N	\N	\N	\N	\N	\N
93	\N	\N	\N	\N	\N	\N	\N	\N	\N
94	\N	\N	\N	\N	\N	\N	\N	\N	\N
95	\N	\N	\N	\N	\N	\N	\N	\N	\N
96	\N	\N	\N	\N	\N	\N	\N	\N	\N
97	\N	\N	\N	\N	\N	\N	\N	\N	\N
98	\N	\N	\N	\N	\N	\N	\N	\N	\N
99	\N	\N	\N	\N	\N	\N	\N	\N	\N
100	\N	\N	\N	\N	\N	\N	\N	\N	\N
101	\N	\N	\N	\N	\N	\N	\N	\N	\N
102	\N	\N	\N	\N	\N	\N	\N	\N	\N
103	\N	\N	\N	\N	\N	\N	\N	\N	\N
104	\N	\N	\N	\N	\N	\N	\N	\N	\N
105	\N	\N	\N	\N	\N	\N	\N	\N	\N
106	\N	\N	\N	\N	\N	\N	\N	\N	\N
107	\N	\N	\N	\N	\N	\N	\N	\N	\N
108	\N	\N	\N	\N	\N	\N	\N	\N	\N
109	\N	\N	\N	\N	\N	\N	\N	\N	\N
\.


--
-- TOC entry 2544 (class 0 OID 28323)
-- Dependencies: 232
-- Data for Name: mpo_icemdebiet; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.mpo_icemdebiet (stand1, stand2, stand3, stand4, stand5, icem_id) FROM stdin;
\N	\N	\N	\N	\N	6
\N	\N	\N	\N	\N	7
\N	\N	\N	\N	\N	8
\N	\N	\N	\N	\N	9
\N	\N	\N	\N	\N	10
\N	\N	\N	\N	\N	11
\N	\N	\N	\N	\N	12
\N	\N	\N	\N	\N	13
\N	\N	\N	\N	\N	14
\N	\N	\N	\N	\N	15
\N	\N	\N	\N	\N	16
\N	\N	\N	\N	\N	17
\N	\N	\N	\N	\N	18
\N	\N	\N	\N	\N	19
\N	\N	\N	\N	\N	20
\N	\N	\N	\N	\N	21
\N	\N	\N	\N	\N	22
\N	\N	\N	\N	\N	23
\N	\N	\N	\N	\N	24
\N	\N	\N	\N	\N	25
\N	\N	\N	\N	\N	26
\N	\N	\N	\N	\N	27
\N	\N	\N	\N	\N	28
\N	\N	\N	\N	\N	29
\N	\N	\N	\N	\N	30
\N	\N	\N	\N	\N	1
\N	\N	\N	\N	\N	2
\N	\N	\N	\N	\N	3
\N	\N	\N	\N	\N	4
\N	\N	\N	\N	\N	5
\N	\N	\N	\N	\N	31
\N	\N	\N	\N	\N	32
\N	\N	\N	\N	\N	33
\N	\N	\N	\N	\N	34
\N	\N	\N	\N	\N	35
\N	\N	\N	\N	\N	36
\N	\N	\N	\N	\N	37
\N	\N	\N	\N	\N	38
\N	\N	\N	\N	\N	39
\N	\N	\N	\N	\N	40
\N	\N	\N	\N	\N	41
\N	\N	\N	\N	\N	42
\N	\N	\N	\N	\N	43
\N	\N	\N	\N	\N	44
\N	\N	\N	\N	\N	45
\N	\N	\N	\N	\N	46
\N	\N	\N	\N	\N	47
\N	\N	\N	\N	\N	48
\N	\N	\N	\N	\N	49
\N	\N	\N	\N	\N	50
\N	\N	\N	\N	\N	51
\N	\N	\N	\N	\N	52
\N	\N	\N	\N	\N	53
\N	\N	\N	\N	\N	54
\N	\N	\N	\N	\N	55
\N	\N	\N	\N	\N	56
\N	\N	\N	\N	\N	57
\N	\N	\N	\N	\N	58
\N	\N	\N	\N	\N	59
\N	\N	\N	\N	\N	60
\N	\N	\N	\N	\N	61
\N	\N	\N	\N	\N	62
\N	\N	\N	\N	\N	63
\N	\N	\N	\N	\N	64
\N	\N	\N	\N	\N	65
\N	\N	\N	\N	\N	66
\N	\N	\N	\N	\N	67
\N	\N	\N	\N	\N	68
\N	\N	\N	\N	\N	69
\N	\N	\N	\N	\N	70
\N	\N	\N	\N	\N	71
\N	\N	\N	\N	\N	72
\N	\N	\N	\N	\N	73
\N	\N	\N	\N	\N	74
\N	\N	\N	\N	\N	75
\N	\N	\N	\N	\N	76
\N	\N	\N	\N	\N	77
\N	\N	\N	\N	\N	78
\N	\N	\N	\N	\N	79
\N	\N	\N	\N	\N	80
\N	\N	\N	\N	\N	81
\N	\N	\N	\N	\N	82
\N	\N	\N	\N	\N	83
\N	\N	\N	\N	\N	84
\N	\N	\N	\N	\N	85
\N	\N	\N	\N	\N	86
\N	\N	\N	\N	\N	87
\N	\N	\N	\N	\N	88
\N	\N	\N	\N	\N	89
\N	\N	\N	\N	\N	90
\N	\N	\N	\N	\N	91
\N	\N	\N	\N	\N	92
\N	\N	\N	\N	\N	93
\N	\N	\N	\N	\N	94
\N	\N	\N	\N	\N	95
\N	\N	\N	\N	\N	96
\N	\N	\N	\N	\N	97
\N	\N	\N	\N	\N	98
\N	\N	\N	\N	\N	99
\N	\N	\N	\N	\N	100
\N	\N	\N	\N	\N	101
\N	\N	\N	\N	\N	102
\N	\N	\N	\N	\N	103
\N	\N	\N	\N	\N	104
\N	\N	\N	\N	\N	105
\N	\N	\N	\N	\N	106
\N	\N	\N	\N	\N	107
\N	\N	\N	\N	\N	108
\N	\N	\N	\N	\N	109
\N	\N	\N	\N	\N	110
\N	\N	\N	\N	\N	111
\N	\N	\N	\N	\N	112
\N	\N	\N	\N	\N	113
\N	\N	\N	\N	\N	114
\N	\N	\N	\N	\N	115
\N	\N	\N	\N	\N	116
\N	\N	\N	\N	\N	117
\N	\N	\N	\N	\N	118
\N	\N	\N	\N	\N	119
\N	\N	\N	\N	\N	120
\N	\N	\N	\N	\N	121
\N	\N	\N	\N	\N	122
\N	\N	\N	\N	\N	123
\N	\N	\N	\N	\N	124
\N	\N	\N	\N	\N	125
\N	\N	\N	\N	\N	126
\N	\N	\N	\N	\N	127
\N	\N	\N	\N	\N	128
\N	\N	\N	\N	\N	129
\N	\N	\N	\N	\N	130
\N	\N	\N	\N	\N	131
\N	\N	\N	\N	\N	132
\N	\N	\N	\N	\N	133
\N	\N	\N	\N	\N	134
\N	\N	\N	\N	\N	135
\N	\N	\N	\N	\N	136
\N	\N	\N	\N	\N	137
\N	\N	\N	\N	\N	138
\N	\N	\N	\N	\N	139
\N	\N	\N	\N	\N	140
\N	\N	\N	\N	\N	141
\N	\N	\N	\N	\N	142
\N	\N	\N	\N	\N	143
\N	\N	\N	\N	\N	144
\N	\N	\N	\N	\N	145
\N	\N	\N	\N	\N	146
\N	\N	\N	\N	\N	147
\N	\N	\N	\N	\N	148
\N	\N	\N	\N	\N	149
\N	\N	\N	\N	\N	150
\N	\N	\N	\N	\N	151
\N	\N	\N	\N	\N	152
\N	\N	\N	\N	\N	153
\N	\N	\N	\N	\N	154
\N	\N	\N	\N	\N	155
\.


--
-- TOC entry 2545 (class 0 OID 28328)
-- Dependencies: 233
-- Data for Name: mpo_omvormer; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.mpo_omvormer ("merkOmvormer", dakheling, capaciteit, owner, levering_door, levering_datum, icem_id) FROM stdin;
\N	\N	\N	\N	\N	\N	6
\N	\N	\N	\N	\N	\N	7
\N	\N	\N	\N	\N	\N	8
\N	\N	\N	\N	\N	\N	9
\N	\N	\N	\N	\N	\N	10
\N	\N	\N	\N	\N	\N	11
\N	\N	\N	\N	\N	\N	12
\N	\N	\N	\N	\N	\N	13
\N	\N	\N	\N	\N	\N	14
\N	\N	\N	\N	\N	\N	15
\N	\N	\N	\N	\N	\N	16
\N	\N	\N	\N	\N	\N	17
\N	\N	\N	\N	\N	\N	18
\N	\N	\N	\N	\N	\N	19
\N	\N	\N	\N	\N	\N	20
\N	\N	\N	\N	\N	\N	21
\N	\N	\N	\N	\N	\N	22
\N	\N	\N	\N	\N	\N	23
\N	\N	\N	\N	\N	\N	24
\N	\N	\N	\N	\N	\N	25
\N	\N	\N	\N	\N	\N	26
\N	\N	\N	\N	\N	\N	27
\N	\N	\N	\N	\N	\N	28
\N	\N	\N	\N	\N	\N	29
\N	\N	\N	\N	\N	\N	30
\N	\N	\N	\N	\N	\N	1
\N	\N	\N	\N	\N	\N	2
\N	\N	\N	\N	\N	\N	3
\N	\N	\N	\N	\N	\N	4
\N	\N	\N	\N	\N	\N	5
\N	\N	\N	\N	\N	\N	31
\N	\N	\N	\N	\N	\N	32
\N	\N	\N	\N	\N	\N	33
\N	\N	\N	\N	\N	\N	34
\N	\N	\N	\N	\N	\N	35
\N	\N	\N	\N	\N	\N	36
\N	\N	\N	\N	\N	\N	37
\N	\N	\N	\N	\N	\N	38
\N	\N	\N	\N	\N	\N	39
\N	\N	\N	\N	\N	\N	40
\N	\N	\N	\N	\N	\N	41
\N	\N	\N	\N	\N	\N	42
\N	\N	\N	\N	\N	\N	43
\N	\N	\N	\N	\N	\N	44
\N	\N	\N	\N	\N	\N	45
\N	\N	\N	\N	\N	\N	46
\N	\N	\N	\N	\N	\N	47
\N	\N	\N	\N	\N	\N	48
\N	\N	\N	\N	\N	\N	49
\N	\N	\N	\N	\N	\N	50
\N	\N	\N	\N	\N	\N	51
\N	\N	\N	\N	\N	\N	52
\N	\N	\N	\N	\N	\N	53
\N	\N	\N	\N	\N	\N	54
\N	\N	\N	\N	\N	\N	55
\N	\N	\N	\N	\N	\N	56
\N	\N	\N	\N	\N	\N	57
\N	\N	\N	\N	\N	\N	58
\N	\N	\N	\N	\N	\N	59
\N	\N	\N	\N	\N	\N	60
\N	\N	\N	\N	\N	\N	61
\N	\N	\N	\N	\N	\N	62
\N	\N	\N	\N	\N	\N	63
\N	\N	\N	\N	\N	\N	64
\N	\N	\N	\N	\N	\N	65
\N	\N	\N	\N	\N	\N	66
\N	\N	\N	\N	\N	\N	67
\N	\N	\N	\N	\N	\N	68
\N	\N	\N	\N	\N	\N	69
\N	\N	\N	\N	\N	\N	70
\N	\N	\N	\N	\N	\N	71
\N	\N	\N	\N	\N	\N	72
\N	\N	\N	\N	\N	\N	73
\N	\N	\N	\N	\N	\N	74
\N	\N	\N	\N	\N	\N	75
\N	\N	\N	\N	\N	\N	76
\N	\N	\N	\N	\N	\N	77
\N	\N	\N	\N	\N	\N	78
\N	\N	\N	\N	\N	\N	79
\N	\N	\N	\N	\N	\N	80
\N	\N	\N	\N	\N	\N	81
\N	\N	\N	\N	\N	\N	82
\N	\N	\N	\N	\N	\N	83
\N	\N	\N	\N	\N	\N	84
\N	\N	\N	\N	\N	\N	85
\N	\N	\N	\N	\N	\N	86
\N	\N	\N	\N	\N	\N	87
\N	\N	\N	\N	\N	\N	88
\N	\N	\N	\N	\N	\N	89
\N	\N	\N	\N	\N	\N	90
\N	\N	\N	\N	\N	\N	91
\N	\N	\N	\N	\N	\N	92
\N	\N	\N	\N	\N	\N	93
\N	\N	\N	\N	\N	\N	94
\N	\N	\N	\N	\N	\N	95
\N	\N	\N	\N	\N	\N	96
\N	\N	\N	\N	\N	\N	97
\N	\N	\N	\N	\N	\N	98
\N	\N	\N	\N	\N	\N	99
\N	\N	\N	\N	\N	\N	100
\N	\N	\N	\N	\N	\N	101
\N	\N	\N	\N	\N	\N	102
\N	\N	\N	\N	\N	\N	103
\N	\N	\N	\N	\N	\N	104
\N	\N	\N	\N	\N	\N	105
\N	\N	\N	\N	\N	\N	106
\N	\N	\N	\N	\N	\N	107
\N	\N	\N	\N	\N	\N	108
\N	\N	\N	\N	\N	\N	109
\N	\N	\N	\N	\N	\N	110
\N	\N	\N	\N	\N	\N	111
\N	\N	\N	\N	\N	\N	112
\N	\N	\N	\N	\N	\N	113
\N	\N	\N	\N	\N	\N	114
\N	\N	\N	\N	\N	\N	115
\N	\N	\N	\N	\N	\N	116
\N	\N	\N	\N	\N	\N	117
\N	\N	\N	\N	\N	\N	118
\N	\N	\N	\N	\N	\N	119
\N	\N	\N	\N	\N	\N	120
\N	\N	\N	\N	\N	\N	121
\N	\N	\N	\N	\N	\N	122
\N	\N	\N	\N	\N	\N	123
\N	\N	\N	\N	\N	\N	124
\N	\N	\N	\N	\N	\N	125
\N	\N	\N	\N	\N	\N	126
\N	\N	\N	\N	\N	\N	127
\N	\N	\N	\N	\N	\N	128
\N	\N	\N	\N	\N	\N	129
\N	\N	\N	\N	\N	\N	130
\N	\N	\N	\N	\N	\N	131
\N	\N	\N	\N	\N	\N	132
\N	\N	\N	\N	\N	\N	133
\N	\N	\N	\N	\N	\N	134
\N	\N	\N	\N	\N	\N	135
\N	\N	\N	\N	\N	\N	136
\N	\N	\N	\N	\N	\N	137
\N	\N	\N	\N	\N	\N	138
\N	\N	\N	\N	\N	\N	139
\N	\N	\N	\N	\N	\N	140
\N	\N	\N	\N	\N	\N	141
\N	\N	\N	\N	\N	\N	142
\N	\N	\N	\N	\N	\N	143
\N	\N	\N	\N	\N	\N	144
\N	\N	\N	\N	\N	\N	145
\N	\N	\N	\N	\N	\N	146
\N	\N	\N	\N	\N	\N	147
\N	\N	\N	\N	\N	\N	148
\N	\N	\N	\N	\N	\N	149
\N	\N	\N	\N	\N	\N	150
\N	\N	\N	\N	\N	\N	151
\N	\N	\N	\N	\N	\N	152
\N	\N	\N	\N	\N	\N	153
\N	\N	\N	\N	\N	\N	154
\N	\N	\N	\N	\N	\N	155
\.


--
-- TOC entry 2546 (class 0 OID 28333)
-- Dependencies: 234
-- Data for Name: mpo_planning; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.mpo_planning (bouwrouting, leverdatum, icem_id) FROM stdin;
1	\N	6
2	\N	7
3	\N	8
4	\N	9
5	\N	10
6	\N	11
7	\N	12
8	\N	13
9	\N	14
10	\N	15
11	\N	16
12	\N	17
13	\N	18
14	\N	19
15	\N	20
16	\N	21
17	\N	22
18	\N	23
19	\N	24
20	\N	25
21	\N	26
22	\N	27
23	\N	28
24	\N	29
25	\N	30
1	\N	1
2	\N	2
3	\N	3
4	\N	4
5	\N	5
26	\N	31
27	\N	32
28	\N	33
29	\N	34
30	\N	35
96	\N	101
97	\N	102
98	\N	103
99	\N	104
100	\N	105
101	\N	106
102	\N	107
103	\N	108
104	\N	109
105	\N	110
106	\N	111
107	\N	112
108	\N	113
109	\N	114
110	\N	115
111	\N	116
112	\N	117
113	\N	118
114	\N	119
115	\N	120
116	\N	121
117	\N	122
118	\N	123
119	\N	124
120	\N	125
121	\N	126
122	\N	127
123	\N	128
124	\N	129
125	\N	130
126	\N	131
127	\N	132
128	\N	133
129	\N	134
130	\N	135
131	\N	136
132	\N	137
133	\N	138
134	\N	139
135	\N	140
136	\N	141
137	\N	142
138	\N	143
139	\N	144
140	\N	145
141	\N	146
142	\N	147
143	\N	148
144	\N	149
145	\N	150
146	\N	151
147	\N	152
148	\N	153
149	\N	154
150	\N	155
31	\N	36
32	\N	37
33	\N	38
34	\N	39
35	\N	40
36	\N	41
37	\N	42
38	\N	43
39	\N	44
40	\N	45
41	\N	46
42	\N	47
43	\N	48
44	\N	49
45	\N	50
46	\N	51
47	\N	52
48	\N	53
49	\N	54
50	\N	55
51	\N	56
52	\N	57
53	\N	58
54	\N	59
55	\N	60
56	\N	61
57	\N	62
58	\N	63
59	\N	64
60	\N	65
61	\N	66
62	\N	67
63	\N	68
64	\N	69
65	\N	70
66	\N	71
67	\N	72
68	\N	73
69	\N	74
70	\N	75
71	\N	76
72	\N	77
73	\N	78
74	\N	79
75	\N	80
76	\N	81
77	\N	82
78	\N	83
79	\N	84
80	\N	85
81	\N	86
82	\N	87
83	\N	88
84	\N	89
85	\N	90
86	\N	91
87	\N	92
88	\N	93
89	\N	94
90	\N	95
91	\N	96
92	\N	97
93	\N	98
94	\N	99
95	\N	100
\.


--
-- TOC entry 2547 (class 0 OID 28338)
-- Dependencies: 235
-- Data for Name: mpo_productiebonstatus; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.mpo_productiebonstatus (icem_id, productiegereed, "productieDatum") FROM stdin;
1	True	\N
2	True	\N
3	True	19-04-2023
4	\N	\N
5	\N	\N
155	\N	\N
154	\N	\N
153	\N	\N
152	\N	\N
151	\N	\N
150	\N	\N
149	\N	\N
148	\N	\N
147	\N	\N
146	\N	\N
145	\N	\N
144	\N	\N
143	\N	\N
142	\N	\N
141	\N	\N
140	\N	\N
139	\N	\N
138	\N	\N
137	\N	\N
136	\N	\N
135	\N	\N
134	\N	\N
133	\N	\N
132	\N	\N
131	\N	\N
130	\N	\N
129	\N	\N
128	\N	\N
127	\N	\N
126	\N	\N
125	\N	\N
124	\N	\N
123	\N	\N
122	\N	\N
121	\N	\N
120	\N	\N
119	\N	\N
118	\N	\N
117	\N	\N
116	\N	\N
115	\N	\N
114	\N	\N
113	\N	\N
112	\N	\N
111	\N	\N
110	\N	\N
109	\N	\N
108	\N	\N
107	\N	\N
106	\N	\N
105	\N	\N
104	\N	\N
103	\N	\N
102	\N	\N
101	\N	\N
100	\N	\N
99	\N	\N
98	\N	\N
97	\N	\N
96	\N	\N
95	\N	\N
94	\N	\N
93	\N	\N
92	\N	\N
91	\N	\N
90	\N	\N
89	\N	\N
88	\N	\N
87	\N	\N
86	\N	\N
85	\N	\N
84	\N	\N
83	\N	\N
82	\N	\N
81	\N	\N
80	\N	\N
79	\N	\N
78	\N	\N
77	\N	\N
76	\N	\N
75	\N	\N
74	\N	\N
73	\N	\N
72	\N	\N
71	\N	\N
70	\N	\N
69	\N	\N
68	\N	\N
67	\N	\N
66	\N	\N
65	\N	\N
64	\N	\N
63	\N	\N
62	\N	\N
61	\N	\N
60	\N	\N
59	\N	\N
58	\N	\N
57	\N	\N
56	\N	\N
55	\N	\N
54	\N	\N
53	\N	\N
52	\N	\N
51	\N	\N
50	\N	\N
49	\N	\N
48	\N	\N
47	\N	\N
46	\N	\N
45	\N	\N
44	\N	\N
43	\N	\N
42	\N	\N
41	\N	\N
40	\N	\N
39	\N	\N
38	\N	\N
37	\N	\N
36	\N	\N
35	\N	\N
34	\N	\N
33	\N	\N
32	\N	\N
31	\N	\N
30	\N	\N
29	\N	\N
28	\N	\N
27	\N	\N
26	\N	\N
25	\N	\N
24	\N	\N
23	\N	\N
22	\N	\N
21	\N	\N
20	\N	\N
19	\N	\N
18	\N	\N
17	\N	\N
16	\N	\N
15	\N	\N
14	\N	\N
13	\N	\N
12	\N	\N
11	\N	\N
10	\N	\N
9	\N	\N
8	\N	\N
7	\N	\N
6	\N	\N
\.


--
-- TOC entry 2548 (class 0 OID 28343)
-- Dependencies: 236
-- Data for Name: mpo_productieexact; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.mpo_productieexact ("bomId", exactnummer, icem_id) FROM stdin;
\N	\N	6
\N	\N	7
\N	\N	8
\N	\N	9
\N	\N	10
\N	\N	11
\N	\N	12
\N	\N	13
\N	\N	14
\N	\N	15
\N	\N	16
\N	\N	17
\N	\N	18
\N	\N	19
\N	\N	20
\N	\N	21
\N	\N	22
\N	\N	23
\N	\N	24
\N	\N	25
\N	\N	26
\N	\N	27
\N	\N	28
\N	\N	29
\N	\N	30
\N	\N	1
\N	\N	2
\N	\N	3
\N	\N	4
\N	\N	5
\N	\N	31
\N	\N	32
\N	\N	33
\N	\N	34
\N	\N	35
\N	\N	36
\N	\N	37
\N	\N	38
\N	\N	39
\N	\N	40
\N	\N	41
\N	\N	42
\N	\N	43
\N	\N	44
\N	\N	45
\N	\N	46
\N	\N	47
\N	\N	48
\N	\N	49
\N	\N	50
\N	\N	51
\N	\N	52
\N	\N	53
\N	\N	54
\N	\N	55
\N	\N	56
\N	\N	57
\N	\N	58
\N	\N	59
\N	\N	60
\N	\N	61
\N	\N	62
\N	\N	63
\N	\N	64
\N	\N	65
\N	\N	66
\N	\N	67
\N	\N	68
\N	\N	69
\N	\N	70
\N	\N	71
\N	\N	72
\N	\N	73
\N	\N	74
\N	\N	75
\N	\N	76
\N	\N	77
\N	\N	78
\N	\N	79
\N	\N	80
\N	\N	81
\N	\N	82
\N	\N	83
\N	\N	84
\N	\N	85
\N	\N	86
\N	\N	87
\N	\N	88
\N	\N	89
\N	\N	90
\N	\N	91
\N	\N	92
\N	\N	93
\N	\N	94
\N	\N	95
\N	\N	96
\N	\N	97
\N	\N	98
\N	\N	99
\N	\N	100
\N	\N	101
\N	\N	102
\N	\N	103
\N	\N	104
\N	\N	105
\N	\N	106
\N	\N	107
\N	\N	108
\N	\N	109
\N	\N	110
\N	\N	111
\N	\N	112
\N	\N	113
\N	\N	114
\N	\N	115
\N	\N	116
\N	\N	117
\N	\N	118
\N	\N	119
\N	\N	120
\N	\N	121
\N	\N	122
\N	\N	123
\N	\N	124
\N	\N	125
\N	\N	126
\N	\N	127
\N	\N	128
\N	\N	129
\N	\N	130
\N	\N	131
\N	\N	132
\N	\N	133
\N	\N	134
\N	\N	135
\N	\N	136
\N	\N	137
\N	\N	138
\N	\N	139
\N	\N	140
\N	\N	141
\N	\N	142
\N	\N	143
\N	\N	144
\N	\N	145
\N	\N	146
\N	\N	147
\N	\N	148
\N	\N	149
\N	\N	150
\N	\N	151
\N	\N	152
\N	\N	153
\N	\N	154
\N	\N	155
\.


--
-- TOC entry 2549 (class 0 OID 28348)
-- Dependencies: 237
-- Data for Name: mpo_semkast; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.mpo_semkast (type, icem_id) FROM stdin;
\N	6
\N	7
\N	8
\N	9
\N	10
\N	11
\N	12
\N	13
\N	14
\N	15
\N	16
\N	17
\N	18
\N	19
\N	20
\N	21
\N	22
\N	23
\N	24
\N	25
\N	26
\N	27
\N	28
\N	29
\N	30
\N	1
\N	2
\N	3
\N	4
\N	5
\N	31
\N	32
\N	33
\N	34
\N	35
\N	36
\N	37
\N	38
\N	39
\N	40
\N	41
\N	42
\N	43
\N	44
\N	45
\N	46
\N	47
\N	48
\N	49
\N	50
\N	51
\N	52
\N	53
\N	54
\N	55
\N	56
\N	57
\N	58
\N	59
\N	60
\N	61
\N	62
\N	63
\N	64
\N	65
\N	66
\N	67
\N	68
\N	69
\N	70
\N	71
\N	72
\N	73
\N	74
\N	75
\N	76
\N	77
\N	78
\N	79
\N	80
\N	81
\N	82
\N	83
\N	84
\N	85
\N	86
\N	87
\N	88
\N	89
\N	90
\N	91
\N	92
\N	93
\N	94
\N	95
\N	96
\N	97
\N	98
\N	99
\N	100
\N	101
\N	102
\N	103
\N	104
\N	105
\N	106
\N	107
\N	108
\N	109
\N	110
\N	111
\N	112
\N	113
\N	114
\N	115
\N	116
\N	117
\N	118
\N	119
\N	120
\N	121
\N	122
\N	123
\N	124
\N	125
\N	126
\N	127
\N	128
\N	129
\N	130
\N	131
\N	132
\N	133
\N	134
\N	135
\N	136
\N	137
\N	138
\N	139
\N	140
\N	141
\N	142
\N	143
\N	144
\N	145
\N	146
\N	147
\N	148
\N	149
\N	150
\N	151
\N	152
\N	153
\N	154
\N	155
\.


--
-- TOC entry 2540 (class 0 OID 28278)
-- Dependencies: 228
-- Data for Name: mpo_site; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.mpo_site (id, bouwnr, blok, straat, huisnr, postcode, bijzonderheden, koop_huur, "projectId_id") FROM stdin;
6	1	A	\N	\N	\N	\N	\N	2
7	2	B	\N	\N	\N	\N	\N	2
8	3	C	\N	\N	\N	\N	\N	2
9	4	D	\N	\N	\N	\N	\N	2
10	5		\N	\N	\N	\N	\N	2
11	6	\N	\N	\N	\N	\N	\N	2
12	7	\N	\N	\N	\N	\N	\N	2
13	8	\N	\N	\N	\N	\N	\N	2
14	9	\N	\N	\N	\N	\N	\N	2
15	10	\N	\N	\N	\N	\N	\N	2
16	11	\N	\N	\N	\N	\N	\N	2
17	12	\N	\N	\N	\N	\N	\N	2
18	13	\N	\N	\N	\N	\N	\N	2
19	14	\N	\N	\N	\N	\N	\N	2
20	15	\N	\N	\N	\N	\N	\N	2
21	16	\N	\N	\N	\N	\N	\N	2
22	17	\N	\N	\N	\N	\N	\N	2
23	18	\N	\N	\N	\N	\N	\N	2
24	19	\N	\N	\N	\N	\N	\N	2
25	20	\N	\N	\N	\N	\N	\N	2
26	21	\N	\N	\N	\N	\N	\N	2
27	22	\N	\N	\N	\N	\N	\N	2
28	23	\N	\N	\N	\N	\N	\N	2
29	24	\N	\N	\N	\N	\N	\N	2
30	25	\N	\N	\N	\N	\N	\N	2
1	1	A	sonoystraat	12	8798BG	Niks bijzonder	Huur	1
2	2	B	steenstraat	102	8765AD	haha	Koop	1
3	3	G	\N	\N	\N	\N	\N	1
4	4	L	\N	\N	\N	\N	\N	1
5	5	A	\N	\N	\N	\N	\N	1
31	26	\N	\N	\N	\N	\N	\N	2
32	27	\N	\N	\N	\N	\N	\N	2
33	28	\N	\N	\N	\N	\N	\N	2
34	29	\N	\N	\N	\N	\N	\N	2
35	30	\N	\N	\N	\N	\N	\N	2
86	81	\N	\N	\N	\N	\N	\N	2
87	82	\N	\N	\N	\N	\N	\N	2
88	83	\N	\N	\N	\N	\N	\N	2
89	84	\N	\N	\N	\N	\N	\N	2
90	85	\N	\N	\N	\N	\N	\N	2
91	86	\N	\N	\N	\N	\N	\N	2
92	87	\N	\N	\N	\N	\N	\N	2
93	88	\N	\N	\N	\N	\N	\N	2
94	89	\N	\N	\N	\N	\N	\N	2
95	90	\N	\N	\N	\N	\N	\N	2
96	91	\N	\N	\N	\N	\N	\N	2
97	92	\N	\N	\N	\N	\N	\N	2
98	93	\N	\N	\N	\N	\N	\N	2
99	94	\N	\N	\N	\N	\N	\N	2
100	95	\N	\N	\N	\N	\N	\N	2
101	96	\N	\N	\N	\N	\N	\N	2
102	97	\N	\N	\N	\N	\N	\N	2
103	98	\N	\N	\N	\N	\N	\N	2
104	99	\N	\N	\N	\N	\N	\N	2
105	100	\N	\N	\N	\N	\N	\N	2
106	101	\N	\N	\N	\N	\N	\N	2
107	102	\N	\N	\N	\N	\N	\N	2
108	103	\N	\N	\N	\N	\N	\N	2
109	104	\N	\N	\N	\N	\N	\N	2
110	105	\N	\N	\N	\N	\N	\N	2
111	106	\N	\N	\N	\N	\N	\N	2
112	107	\N	\N	\N	\N	\N	\N	2
113	108	\N	\N	\N	\N	\N	\N	2
114	109	\N	\N	\N	\N	\N	\N	2
115	110	\N	\N	\N	\N	\N	\N	2
116	111	\N	\N	\N	\N	\N	\N	2
117	112	\N	\N	\N	\N	\N	\N	2
36	31	\N	\N	\N	\N	\N	\N	2
37	32	\N	\N	\N	\N	\N	\N	2
38	33	\N	\N	\N	\N	\N	\N	2
39	34	\N	\N	\N	\N	\N	\N	2
40	35	\N	\N	\N	\N	\N	\N	2
41	36	\N	\N	\N	\N	\N	\N	2
42	37	\N	\N	\N	\N	\N	\N	2
43	38	\N	\N	\N	\N	\N	\N	2
44	39	\N	\N	\N	\N	\N	\N	2
45	40	\N	\N	\N	\N	\N	\N	2
46	41	\N	\N	\N	\N	\N	\N	2
47	42	\N	\N	\N	\N	\N	\N	2
48	43	\N	\N	\N	\N	\N	\N	2
49	44	\N	\N	\N	\N	\N	\N	2
50	45	\N	\N	\N	\N	\N	\N	2
51	46	\N	\N	\N	\N	\N	\N	2
52	47	\N	\N	\N	\N	\N	\N	2
53	48	\N	\N	\N	\N	\N	\N	2
54	49	\N	\N	\N	\N	\N	\N	2
55	50	\N	\N	\N	\N	\N	\N	2
56	51	\N	\N	\N	\N	\N	\N	2
57	52	\N	\N	\N	\N	\N	\N	2
58	53	\N	\N	\N	\N	\N	\N	2
59	54	\N	\N	\N	\N	\N	\N	2
60	55	\N	\N	\N	\N	\N	\N	2
61	56	\N	\N	\N	\N	\N	\N	2
62	57	\N	\N	\N	\N	\N	\N	2
63	58	\N	\N	\N	\N	\N	\N	2
64	59	\N	\N	\N	\N	\N	\N	2
65	60	\N	\N	\N	\N	\N	\N	2
66	61	\N	\N	\N	\N	\N	\N	2
67	62	\N	\N	\N	\N	\N	\N	2
68	63	\N	\N	\N	\N	\N	\N	2
69	64	\N	\N	\N	\N	\N	\N	2
70	65	\N	\N	\N	\N	\N	\N	2
71	66	\N	\N	\N	\N	\N	\N	2
72	67	\N	\N	\N	\N	\N	\N	2
73	68	\N	\N	\N	\N	\N	\N	2
74	69	\N	\N	\N	\N	\N	\N	2
75	70	\N	\N	\N	\N	\N	\N	2
76	71	\N	\N	\N	\N	\N	\N	2
77	72	\N	\N	\N	\N	\N	\N	2
78	73	\N	\N	\N	\N	\N	\N	2
79	74	\N	\N	\N	\N	\N	\N	2
80	75	\N	\N	\N	\N	\N	\N	2
81	76	\N	\N	\N	\N	\N	\N	2
82	77	\N	\N	\N	\N	\N	\N	2
83	78	\N	\N	\N	\N	\N	\N	2
84	79	\N	\N	\N	\N	\N	\N	2
85	80	\N	\N	\N	\N	\N	\N	2
118	113	\N	\N	\N	\N	\N	\N	2
119	114	\N	\N	\N	\N	\N	\N	2
120	115	\N	\N	\N	\N	\N	\N	2
121	116	\N	\N	\N	\N	\N	\N	2
122	117	\N	\N	\N	\N	\N	\N	2
123	118	\N	\N	\N	\N	\N	\N	2
124	119	\N	\N	\N	\N	\N	\N	2
125	120	\N	\N	\N	\N	\N	\N	2
126	121	\N	\N	\N	\N	\N	\N	2
127	122	\N	\N	\N	\N	\N	\N	2
128	123	\N	\N	\N	\N	\N	\N	2
129	124	\N	\N	\N	\N	\N	\N	2
130	125	\N	\N	\N	\N	\N	\N	2
131	126	\N	\N	\N	\N	\N	\N	2
132	127	\N	\N	\N	\N	\N	\N	2
133	128	\N	\N	\N	\N	\N	\N	2
134	129	\N	\N	\N	\N	\N	\N	2
135	130	\N	\N	\N	\N	\N	\N	2
136	131	\N	\N	\N	\N	\N	\N	2
137	132	\N	\N	\N	\N	\N	\N	2
138	133	\N	\N	\N	\N	\N	\N	2
139	134	\N	\N	\N	\N	\N	\N	2
140	135	\N	\N	\N	\N	\N	\N	2
141	136	\N	\N	\N	\N	\N	\N	2
142	137	\N	\N	\N	\N	\N	\N	2
143	138	\N	\N	\N	\N	\N	\N	2
144	139	\N	\N	\N	\N	\N	\N	2
145	140	\N	\N	\N	\N	\N	\N	2
146	141	\N	\N	\N	\N	\N	\N	2
147	142	\N	\N	\N	\N	\N	\N	2
148	143	\N	\N	\N	\N	\N	\N	2
149	144	\N	\N	\N	\N	\N	\N	2
150	145	\N	\N	\N	\N	\N	\N	2
151	146	\N	\N	\N	\N	\N	\N	2
152	147	\N	\N	\N	\N	\N	\N	2
153	148	\N	\N	\N	\N	\N	\N	2
154	149	\N	\N	\N	\N	\N	\N	2
155	150	\N	\N	\N	\N	\N	\N	2
\.


--
-- TOC entry 2596 (class 0 OID 0)
-- Dependencies: 227
-- Name: mpo_site_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.mpo_site_id_seq', 155, true);


--
-- TOC entry 2550 (class 0 OID 28353)
-- Dependencies: 238
-- Data for Name: mpo_warmtepomp; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.mpo_warmtepomp (vermogen, icem_id) FROM stdin;
\N	6
\N	7
\N	8
\N	9
\N	10
\N	11
\N	12
\N	13
\N	14
\N	15
\N	16
\N	17
\N	18
\N	19
\N	20
\N	21
\N	22
\N	23
\N	24
\N	25
\N	26
\N	27
\N	28
\N	29
\N	30
\N	1
\N	2
\N	3
8	4
7	5
\N	31
\N	32
\N	33
\N	34
\N	35
\N	36
\N	37
\N	38
\N	39
\N	40
\N	41
\N	42
\N	43
\N	44
\N	45
\N	46
\N	47
\N	48
\N	49
\N	50
\N	51
\N	52
\N	53
\N	54
\N	55
\N	56
\N	57
\N	58
\N	59
\N	60
\N	61
\N	62
\N	63
\N	64
\N	65
\N	66
\N	67
\N	68
\N	69
\N	70
\N	71
\N	72
\N	73
\N	74
\N	75
\N	76
\N	77
\N	78
\N	79
\N	80
\N	81
\N	82
\N	83
\N	84
\N	85
\N	86
\N	87
\N	88
\N	89
\N	90
\N	91
\N	92
\N	93
\N	94
\N	95
\N	96
\N	97
\N	98
\N	99
\N	100
\N	101
\N	102
\N	103
\N	104
\N	105
\N	106
\N	107
\N	108
\N	109
\N	110
\N	111
\N	112
\N	113
\N	114
\N	115
\N	116
\N	117
\N	118
\N	119
\N	120
\N	121
\N	122
\N	123
\N	124
\N	125
\N	126
\N	127
\N	128
\N	129
\N	130
\N	131
\N	132
\N	133
\N	134
\N	135
\N	136
\N	137
\N	138
\N	139
\N	140
\N	141
\N	142
\N	143
\N	144
\N	145
\N	146
\N	147
\N	148
\N	149
\N	150
\N	151
\N	152
\N	153
\N	154
\N	155
\.


--
-- TOC entry 2551 (class 0 OID 28358)
-- Dependencies: 239
-- Data for Name: mpo_wtw; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.mpo_wtw (merk, type, debiet, icem_id) FROM stdin;
\N	\N	\N	6
\N	\N	\N	7
\N	\N	\N	8
\N	\N	\N	9
\N	\N	\N	10
\N	\N	\N	11
\N	\N	\N	12
\N	\N	\N	13
\N	\N	\N	14
\N	\N	\N	15
\N	\N	\N	16
\N	\N	\N	17
\N	\N	\N	18
\N	\N	\N	19
\N	\N	\N	20
\N	\N	\N	21
\N	\N	\N	22
\N	\N	\N	23
\N	\N	\N	24
\N	\N	\N	25
\N	\N	\N	26
\N	\N	\N	27
\N	\N	\N	28
\N	\N	\N	29
\N	\N	\N	30
Renovent	4/0 Links	600	1
\N	\N	709	2
\N	\N	\N	3
\N	\N	\N	4
\N	\N	\N	5
\N	\N	\N	31
\N	\N	\N	32
\N	\N	\N	33
\N	\N	\N	34
\N	\N	\N	35
\N	\N	\N	36
\N	\N	\N	37
\N	\N	\N	38
\N	\N	\N	39
\N	\N	\N	40
\N	\N	\N	41
\N	\N	\N	42
\N	\N	\N	43
\N	\N	\N	44
\N	\N	\N	45
\N	\N	\N	46
\N	\N	\N	47
\N	\N	\N	48
\N	\N	\N	49
\N	\N	\N	50
\N	\N	\N	51
\N	\N	\N	52
\N	\N	\N	53
\N	\N	\N	54
\N	\N	\N	55
\N	\N	\N	56
\N	\N	\N	57
\N	\N	\N	58
\N	\N	\N	59
\N	\N	\N	60
\N	\N	\N	61
\N	\N	\N	62
\N	\N	\N	63
\N	\N	\N	64
\N	\N	\N	65
\N	\N	\N	66
\N	\N	\N	67
\N	\N	\N	68
\N	\N	\N	69
\N	\N	\N	70
\N	\N	\N	71
\N	\N	\N	72
\N	\N	\N	73
\N	\N	\N	74
\N	\N	\N	75
\N	\N	\N	76
\N	\N	\N	77
\N	\N	\N	78
\N	\N	\N	79
\N	\N	\N	80
\N	\N	\N	81
\N	\N	\N	82
\N	\N	\N	83
\N	\N	\N	84
\N	\N	\N	85
\N	\N	\N	86
\N	\N	\N	87
\N	\N	\N	88
\N	\N	\N	89
\N	\N	\N	90
\N	\N	\N	91
\N	\N	\N	92
\N	\N	\N	93
\N	\N	\N	94
\N	\N	\N	95
\N	\N	\N	96
\N	\N	\N	97
\N	\N	\N	98
\N	\N	\N	99
\N	\N	\N	100
\N	\N	\N	101
\N	\N	\N	102
\N	\N	\N	103
\N	\N	\N	104
\N	\N	\N	105
\N	\N	\N	106
\N	\N	\N	107
\N	\N	\N	108
\N	\N	\N	109
\N	\N	\N	110
\N	\N	\N	111
\N	\N	\N	112
\N	\N	\N	113
\N	\N	\N	114
\N	\N	\N	115
\N	\N	\N	116
\N	\N	\N	117
\N	\N	\N	118
\N	\N	\N	119
\N	\N	\N	120
\N	\N	\N	121
\N	\N	\N	122
\N	\N	\N	123
\N	\N	\N	124
\N	\N	\N	125
\N	\N	\N	126
\N	\N	\N	127
\N	\N	\N	128
\N	\N	\N	129
\N	\N	\N	130
\N	\N	\N	131
\N	\N	\N	132
\N	\N	\N	133
\N	\N	\N	134
\N	\N	\N	135
\N	\N	\N	136
\N	\N	\N	137
\N	\N	\N	138
\N	\N	\N	139
\N	\N	\N	140
\N	\N	\N	141
\N	\N	\N	142
\N	\N	\N	143
\N	\N	\N	144
\N	\N	\N	145
\N	\N	\N	146
\N	\N	\N	147
\N	\N	\N	148
\N	\N	\N	149
\N	\N	\N	150
\N	\N	\N	151
\N	\N	\N	152
\N	\N	\N	153
\N	\N	\N	154
\N	\N	\N	155
\.


--
-- TOC entry 2553 (class 0 OID 28412)
-- Dependencies: 241
-- Data for Name: opleverrapport_opleverrapport; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.opleverrapport_opleverrapport (id, last_edit_datum, druktest, vacumeren, datatest_npi_tool, pragrammeren_warmtepomp, "testHomecontroller", doorvoeren_afgedicht, leiding_afgedopt, reinigen_module, visuele_inspectie_binnenzijde, visuele_inspectie_buitenzijde, bouwrouting_op_unit, transportklarr_gemaakt, router, poe24v, poe48v, din_rail, utp_kabel_groen, utp_kabel_blauw, utp_kabel_grijs, utp_kabel_zwart, boilersensor, th1_kabel_display_kabel, "homeController_set", omvormer, sem_kast, kwh_meter, p5stekker_omvormer, kampstrup_meter_21, landis_gyr_meter, wtw, soft_encloser, tongdy, procon, antenne, afvoer_flexbuis_slang, sifon, rode_sensor, grijs_zwart_sensor, aansluitslang_zwart, lange_schroeven, vilblokjes_oranje, flow_sensor, doorlock, plexiplaat_e_module, wielen, opleverrapport_definitief, opleverrapport_definitief_datum, author_id, project_id, site_id) FROM stdin;
1	29-04-2023	t	t	t	t	t	t	t	t	t	t	t	t	t	t	t	t	t	t	t	t	t	t	t	t	t	t	t	t	t	t	t	t	t	t	t	t	t	t	t	t	t	t	t	t	t	f		7	1	1
\.


--
-- TOC entry 2597 (class 0 OID 0)
-- Dependencies: 240
-- Name: opleverrapport_opleverrapport_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.opleverrapport_opleverrapport_id_seq', 1, true);


--
-- TOC entry 2524 (class 0 OID 28206)
-- Dependencies: 212
-- Data for Name: project_klant; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.project_klant (id, klantnaam, plaats, land, provincie, phone) FROM stdin;
1	Giesbers-Wijchen Bouw B.V	Zouterwoude	Nederland	Noord-Holland	3168765437823
2	Emergo Energiesystemen B.V	Arnhem	Nederland	Gelderland	+31698784367
\.


--
-- TOC entry 2598 (class 0 OID 0)
-- Dependencies: 211
-- Name: project_klant_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.project_klant_id_seq', 2, true);


--
-- TOC entry 2526 (class 0 OID 28214)
-- Dependencies: 214
-- Data for Name: project_klantmedewerker; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.project_klantmedewerker (id, name_medewerker, achternaam_medewerker, phone, functie_medewerker, "klantID_id") FROM stdin;
1	John	Doe	31689438923	Projectleider	1
2	Handricks	Lammer	31687436743	Projectleider	2
3	John	Ngenzi	31687546754	Werk-voorbereider	2
4	Garison	Maze	31687438932	Uitvoerder	2
\.


--
-- TOC entry 2599 (class 0 OID 0)
-- Dependencies: 213
-- Name: project_klantmedewerker_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.project_klantmedewerker_id_seq', 4, true);


--
-- TOC entry 2528 (class 0 OID 28222)
-- Dependencies: 216
-- Data for Name: project_onderaanemerbedrijf; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.project_onderaanemerbedrijf (id, naam) FROM stdin;
1	Bedrijf 1
2	Bedrijf1
3	Bedrijf 1
\.


--
-- TOC entry 2600 (class 0 OID 0)
-- Dependencies: 215
-- Name: project_onderaanemerbedrijf_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.project_onderaanemerbedrijf_id_seq', 3, true);


--
-- TOC entry 2530 (class 0 OID 28230)
-- Dependencies: 218
-- Data for Name: project_project; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.project_project (id, projectnr, projectnaam, plaats, provincie, land, "projectStatus", offertenr, exactnr, debiteurnr, renovatie_nieuwbouw, "selectedWerkvoorbereiderFz", "selectedProjecleiderFz", inopdrachtvoor_vloerverwarming, inopdrachtvoor_ventilatieinstallatie, inopdrachtvoor_zonnepanelen, "datumSystemInvoer", "startDatum", offertedatum, "uitlijkDatumOpdrachtIndienWTW", "uitlijkDatumOpdrachtAlleenICEM", opmerking, klant_id) FROM stdin;
1	23001	5 Woningen Dussen	Dussen	Gelderland	Nederland	Onderhandeling	65874	9876	\N	Renovatie	10	8	FZ	\N	\N	24-04-2023	2023-04-14	01-01-1970	01-01-1970	01-01-1970		1
2	23002	150 woningen Arnhem	Arnhem	Gelderland	Nederland	Offerte	LG8765	876543	GDF6765	Nieuwbouw	10	8	FZ	Derden	Derden	29-04-2023	07-05-2023	07-05-2023	06-05-2023	04-05-2023	Project number 2	2
\.


--
-- TOC entry 2601 (class 0 OID 0)
-- Dependencies: 217
-- Name: project_project_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.project_project_id_seq', 2, true);


--
-- TOC entry 2532 (class 0 OID 28243)
-- Dependencies: 220
-- Data for Name: project_projecticem; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.project_projecticem (id, "iNumber", "pNumber", "eNumber", "fNumber", "aNumber", "totaalNumber", "estimatedValue", project_id) FROM stdin;
\.


--
-- TOC entry 2602 (class 0 OID 0)
-- Dependencies: 219
-- Name: project_projecticem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.project_projecticem_id_seq', 1, false);


--
-- TOC entry 2534 (class 0 OID 28251)
-- Dependencies: 222
-- Data for Name: project_statusonderaanemer; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.project_statusonderaanemer (id, status, odernummer, onderaanemer_id, project_id_id) FROM stdin;
2	vloerverwarming	65476	1	1
3	vloerverwarming	75658	1	2
\.


--
-- TOC entry 2603 (class 0 OID 0)
-- Dependencies: 221
-- Name: project_statusonderaanemer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.project_statusonderaanemer_id_seq', 4, true);


--
-- TOC entry 2536 (class 0 OID 28259)
-- Dependencies: 224
-- Data for Name: project_vertegenwoordiger_project; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.project_vertegenwoordiger_project (id, projectnr, vertegenwoordiger_id) FROM stdin;
\.


--
-- TOC entry 2604 (class 0 OID 0)
-- Dependencies: 223
-- Name: project_vertegenwoordiger_project_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.project_vertegenwoordiger_project_id_seq', 1, false);


--
-- TOC entry 2556 (class 0 OID 28519)
-- Dependencies: 244
-- Data for Name: testrapport_testrapport; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.testrapport_testrapport (id, last_edit_datum, druktest, druktest_datum, luchtest, luchtest_datum, druk_cv, flow_cv, standtijd_cv, druktap, standtijd_druktap, npidatatestuitgevoerd, npidatatesuitgevoerd_datum, "programmeerSD_kaart", aanvoertemp, tijd_legionella, frame, sem_gateway, sem_mac_adres, warmtepomp_binnen_ftc_unit, warmtepomp_buiten, procon, ventilatie_wtw, kamstrup_21_rond, kamstrup_403_landis_t230, flowmeter, display_mac_adres_homecontroller, boiler, spinvlies_voldoende, bekabeling_voldoende, lekvrij_door_blower_door_test, spinvlies_zijkanten, eindschoonmaak_binnenzijde, stikstof_en_vacumeren_module, stikstof_sterkte_bar, stikstof_sterkte_standtijd, vacumeren_module_micron, vacumeren_module_standtijd, lekdetectie, lekdetectie_datum, sn_label_op_frame, wtw_debieten_control, transportlabel_uitgevoerd, eindschoonmaak_uitgevoerd, transport_gereed, transport_gereed_datum, eindcontrole, eindcontrole_datum, testrapport_definitief, testrapport_definitief_datum, author_id, project_id, site_id) FROM stdin;
1	28-04-2023	t	2023-04-11	t	2023-04-12			01:15		22:18	f		f	0	23:36	frame	gateway	8494848488										f	f	f	f	f						t	2023-04-29	t	t	f	f	t	2023-04-26	t	2023-04-23	f		7	1	1
\.


--
-- TOC entry 2605 (class 0 OID 0)
-- Dependencies: 243
-- Name: testrapport_testrapport_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.testrapport_testrapport_id_seq', 1, true);


--
-- TOC entry 2508 (class 0 OID 28070)
-- Dependencies: 196
-- Data for Name: users_customuser; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users_customuser (id, password, is_superuser, email, is_active, date_joined, is_loggedin, last_login, is_staff, functie_id) FROM stdin;
5	pbkdf2_sha256$260000$0KqOT5NekjSSK3e9IgW3px$zEy5yNdnDhDXDs8q4ojhsf690WTC+OuxE3NMmwuztmM=	f	symen@factoryzero.nl	t	2023-04-21 17:08:02.916084+02	f	2023-04-21 20:48:00+02	t	1
3	pbkdf2_sha256$260000$5IIsTaARGkczWFUOHLuSXV$DRJzm+/mY0AQyUCEP0tGaZv2wrGFtCj+agC+RH1JFfE=	f	rico@factoryzero.nl	t	2023-04-21 16:53:39.091655+02	f	2023-04-21 19:40:58+02	t	1
4	pbkdf2_sha256$260000$qF17RHRalFeRndkjof9Gh0$Yoyg/AWU1XXjbXtFyJpaoLyvJaK1E6nb8STxA8/rYNE=	f	rico2@factoryzero.nl	t	2023-04-21 17:01:30.528295+02	f	1900-01-01 11:20:30+01	t	1
2	pbkdf2_sha256$260000$6AZMi09RCUqJ1S14UgnH0w$hAzgefHiPuBawokyVHZIkBCVEqXv4J9M12YBn9kbZv4=	f	nia@factoryzero.nl	t	2023-04-21 16:46:14.881268+02	f	1900-01-01 11:20:30+01	t	1
11	pbkdf2_sha256$260000$JWyb49v5ATKa0oS6oUmnkE$/DbJDz3iIgJ95uOGkxl03FueueWDVBYwWUuwhCyl49o=	f	mariam@factoryzero.nl	t	2023-04-24 10:49:13.674042+02	f	1900-01-01 11:20:30+01	t	3
9	pbkdf2_sha256$260000$qAMaasKJ90g3L7wDDJcOlX$sKwaGRS2Mf1Q1b46IvyWGfygjHHBu3iJgkrTPf8wTT4=	f	minah@factoryzero.nl	t	2023-04-24 08:48:53.646724+02	f	1900-01-01 11:20:30+01	t	2
6	pbkdf2_sha256$260000$3FqmPDJqYHKxF2qEZYzatv$A6zHreSJ4dUN/spfSYf9cXx1J2oQ1hd7RjIzVFn+cUA=	f	lol@factoryzero.nl	t	2023-04-21 17:37:44.597293+02	f	1900-01-01 11:20:30+01	t	1
1	pbkdf2_sha256$260000$HIEoXlGvm7rQo9Ku7Ol9qz$7zPMCP0LA1HeynmY0mAlHjhoKz4uAo6ZKFy0Qry11iU=	t	yvan@factoryzero.nl	t	2023-04-20 16:00:59.946274+02	f	2023-04-30 21:05:10+02	t	1
8	pbkdf2_sha256$260000$xNZhUdYtbp6Al662iSECFc$xrBBWSsR/jrNUGVqViKHJrqxzYbYWt2xRCco9diw5rU=	f	tadjer@factoryzero.nl	t	2023-04-22 15:24:22.604314+02	t	2023-04-30 21:05:42.186826+02	t	1
10	pbkdf2_sha256$260000$29xlwq1qB9BzL6RlPkNW7J$Ei0SXbU77aUMkyL4sZLQQkV8XAk4fw5J5Fy9KHBsQsY=	f	ruben@factoryzero.nl	t	2023-04-24 08:53:30.454131+02	f	1900-01-01 11:20:30+01	t	2
7	pbkdf2_sha256$260000$vfPswV3ALff8K9QrZlkJlD$P/XKh4tt0kwLKTC0Q/kDM3IsWJDiTEXTmdWt1B7F3tw=	f	muammer@factoryzero.nl	t	2023-04-21 19:50:39.863261+02	f	2023-04-26 09:41:21+02	t	1
\.


--
-- TOC entry 2518 (class 0 OID 28125)
-- Dependencies: 206
-- Data for Name: users_customuser_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users_customuser_groups (id, customuser_id, group_id) FROM stdin;
\.


--
-- TOC entry 2606 (class 0 OID 0)
-- Dependencies: 205
-- Name: users_customuser_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_customuser_groups_id_seq', 1, false);


--
-- TOC entry 2607 (class 0 OID 0)
-- Dependencies: 195
-- Name: users_customuser_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_customuser_id_seq', 11, true);


--
-- TOC entry 2520 (class 0 OID 28133)
-- Dependencies: 208
-- Data for Name: users_customuser_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users_customuser_user_permissions (id, customuser_id, permission_id) FROM stdin;
1	5	21
2	5	22
3	5	31
4	6	24
5	6	29
6	7	23
7	7	24
8	7	32
9	8	5
10	9	56
11	9	53
12	10	53
13	10	56
14	11	56
15	11	54
\.


--
-- TOC entry 2608 (class 0 OID 0)
-- Dependencies: 207
-- Name: users_customuser_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_customuser_user_permissions_id_seq', 15, true);


--
-- TOC entry 2516 (class 0 OID 28112)
-- Dependencies: 204
-- Data for Name: users_functie; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users_functie (id, functie, rol_id) FROM stdin;
1	Engineer	1
2	Projectleider	2
3	Werkvoor-bereider	3
\.


--
-- TOC entry 2609 (class 0 OID 0)
-- Dependencies: 203
-- Name: users_functie_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_functie_id_seq', 3, true);


--
-- TOC entry 2510 (class 0 OID 28080)
-- Dependencies: 198
-- Data for Name: users_klantwoningbouw; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users_klantwoningbouw (id, name, phone_no, fax_number, straat, postcode, provincie, land) FROM stdin;
\.


--
-- TOC entry 2610 (class 0 OID 0)
-- Dependencies: 197
-- Name: users_klantwoningbouw_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_klantwoningbouw_id_seq', 1, false);


--
-- TOC entry 2514 (class 0 OID 28099)
-- Dependencies: 202
-- Data for Name: users_medewerkerprofile; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users_medewerkerprofile (id, voornaam, voorletter, tussenvoegsel, achternaam, geslacht, geboortdatum, phone_no, fax_number, user_id) FROM stdin;
1	Yvan	Y	Van	Mutara	Dhr	24-05-1988	+31687621114		1
2	Nia	N		Mutara	Mevr	2023-04-18	+31678439823		2
3	Rico	R		Man	Dhr	2023-04-19	+31763363633		3
5	Symen	S		Jansen	Dhr	2023-04-18	+31764746473		5
6	Muammer	M		Kirikou	Dhr	2023-04-12	+31687678943		7
7	Tadjer	T		Admin	Dhr	1991-05-24	+31687546732		8
8	Minah	M		Salim	Dhr	1998-06-18	+3168754984378		9
9	Ruben	R		Crespo	Dhr	2003-06-18	+31687549832		10
4	John			Connor	Dhr	2021-04-13	+31650589692		4
10	Mariam	M		Salum	Mevr	1986-04-23	+31697645324		11
\.


--
-- TOC entry 2611 (class 0 OID 0)
-- Dependencies: 201
-- Name: users_medewerkerprofile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_medewerkerprofile_id_seq', 10, true);


--
-- TOC entry 2512 (class 0 OID 28088)
-- Dependencies: 200
-- Data for Name: users_role; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users_role (id, role_name) FROM stdin;
1	R&D
2	Projectleider
3	Bedrijfsbureau
\.


--
-- TOC entry 2612 (class 0 OID 0)
-- Dependencies: 199
-- Name: users_role_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_role_id_seq', 3, true);


--
-- TOC entry 2233 (class 2606 OID 28066)
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- TOC entry 2238 (class 2606 OID 28052)
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- TOC entry 2241 (class 2606 OID 28041)
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- TOC entry 2235 (class 2606 OID 28031)
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- TOC entry 2228 (class 2606 OID 28043)
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- TOC entry 2230 (class 2606 OID 28023)
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- TOC entry 2273 (class 2606 OID 28191)
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- TOC entry 2223 (class 2606 OID 28015)
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- TOC entry 2225 (class 2606 OID 28013)
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- TOC entry 2221 (class 2606 OID 28005)
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- TOC entry 2336 (class 2606 OID 28514)
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- TOC entry 2300 (class 2606 OID 28275)
-- Name: mpo_bewoners mpo_bewoners_email_bewoner_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mpo_bewoners
    ADD CONSTRAINT mpo_bewoners_email_bewoner_key UNIQUE (email_bewoner);


--
-- TOC entry 2302 (class 2606 OID 28273)
-- Name: mpo_bewoners mpo_bewoners_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mpo_bewoners
    ADD CONSTRAINT mpo_bewoners_pkey PRIMARY KEY (id);


--
-- TOC entry 2312 (class 2606 OID 28322)
-- Name: mpo_boiler mpo_boiler_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mpo_boiler
    ADD CONSTRAINT mpo_boiler_pkey PRIMARY KEY (icem_id);


--
-- TOC entry 2308 (class 2606 OID 28291)
-- Name: mpo_bouwkundig mpo_bouwkundig_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mpo_bouwkundig
    ADD CONSTRAINT mpo_bouwkundig_pkey PRIMARY KEY (site_id);


--
-- TOC entry 2310 (class 2606 OID 28296)
-- Name: mpo_icem mpo_icem_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mpo_icem
    ADD CONSTRAINT mpo_icem_pkey PRIMARY KEY (site_id);


--
-- TOC entry 2314 (class 2606 OID 28327)
-- Name: mpo_icemdebiet mpo_icemdebiet_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mpo_icemdebiet
    ADD CONSTRAINT mpo_icemdebiet_pkey PRIMARY KEY (icem_id);


--
-- TOC entry 2316 (class 2606 OID 28332)
-- Name: mpo_omvormer mpo_omvormer_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mpo_omvormer
    ADD CONSTRAINT mpo_omvormer_pkey PRIMARY KEY (icem_id);


--
-- TOC entry 2318 (class 2606 OID 28337)
-- Name: mpo_planning mpo_planning_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mpo_planning
    ADD CONSTRAINT mpo_planning_pkey PRIMARY KEY (icem_id);


--
-- TOC entry 2320 (class 2606 OID 28342)
-- Name: mpo_productiebonstatus mpo_productiebonstatus_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mpo_productiebonstatus
    ADD CONSTRAINT mpo_productiebonstatus_pkey PRIMARY KEY (icem_id);


--
-- TOC entry 2322 (class 2606 OID 28347)
-- Name: mpo_productieexact mpo_productieexact_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mpo_productieexact
    ADD CONSTRAINT mpo_productieexact_pkey PRIMARY KEY (icem_id);


--
-- TOC entry 2324 (class 2606 OID 28352)
-- Name: mpo_semkast mpo_semkast_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mpo_semkast
    ADD CONSTRAINT mpo_semkast_pkey PRIMARY KEY (icem_id);


--
-- TOC entry 2305 (class 2606 OID 28286)
-- Name: mpo_site mpo_site_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mpo_site
    ADD CONSTRAINT mpo_site_pkey PRIMARY KEY (id);


--
-- TOC entry 2326 (class 2606 OID 28357)
-- Name: mpo_warmtepomp mpo_warmtepomp_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mpo_warmtepomp
    ADD CONSTRAINT mpo_warmtepomp_pkey PRIMARY KEY (icem_id);


--
-- TOC entry 2328 (class 2606 OID 28362)
-- Name: mpo_wtw mpo_wtw_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mpo_wtw
    ADD CONSTRAINT mpo_wtw_pkey PRIMARY KEY (icem_id);


--
-- TOC entry 2331 (class 2606 OID 28417)
-- Name: opleverrapport_opleverrapport opleverrapport_opleverrapport_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.opleverrapport_opleverrapport
    ADD CONSTRAINT opleverrapport_opleverrapport_pkey PRIMARY KEY (id);


--
-- TOC entry 2276 (class 2606 OID 28211)
-- Name: project_klant project_klant_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.project_klant
    ADD CONSTRAINT project_klant_pkey PRIMARY KEY (id);


--
-- TOC entry 2279 (class 2606 OID 28219)
-- Name: project_klantmedewerker project_klantmedewerker_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.project_klantmedewerker
    ADD CONSTRAINT project_klantmedewerker_pkey PRIMARY KEY (id);


--
-- TOC entry 2281 (class 2606 OID 28227)
-- Name: project_onderaanemerbedrijf project_onderaanemerbedrijf_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.project_onderaanemerbedrijf
    ADD CONSTRAINT project_onderaanemerbedrijf_pkey PRIMARY KEY (id);


--
-- TOC entry 2284 (class 2606 OID 28238)
-- Name: project_project project_project_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.project_project
    ADD CONSTRAINT project_project_pkey PRIMARY KEY (id);


--
-- TOC entry 2287 (class 2606 OID 28240)
-- Name: project_project project_project_projectnr_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.project_project
    ADD CONSTRAINT project_project_projectnr_key UNIQUE (projectnr);


--
-- TOC entry 2289 (class 2606 OID 28248)
-- Name: project_projecticem project_projecticem_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.project_projecticem
    ADD CONSTRAINT project_projecticem_pkey PRIMARY KEY (id);


--
-- TOC entry 2293 (class 2606 OID 28256)
-- Name: project_statusonderaanemer project_statusonderaanemer_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.project_statusonderaanemer
    ADD CONSTRAINT project_statusonderaanemer_pkey PRIMARY KEY (id);


--
-- TOC entry 2296 (class 2606 OID 28264)
-- Name: project_vertegenwoordiger_project project_vertegenwoordiger_project_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.project_vertegenwoordiger_project
    ADD CONSTRAINT project_vertegenwoordiger_project_pkey PRIMARY KEY (id);


--
-- TOC entry 2340 (class 2606 OID 28527)
-- Name: testrapport_testrapport testrapport_testrapport_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.testrapport_testrapport
    ADD CONSTRAINT testrapport_testrapport_pkey PRIMARY KEY (id);


--
-- TOC entry 2244 (class 2606 OID 28077)
-- Name: users_customuser users_customuser_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_customuser
    ADD CONSTRAINT users_customuser_email_key UNIQUE (email);


--
-- TOC entry 2261 (class 2606 OID 28153)
-- Name: users_customuser_groups users_customuser_groups_customuser_id_group_id_76b619e3_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_customuser_groups
    ADD CONSTRAINT users_customuser_groups_customuser_id_group_id_76b619e3_uniq UNIQUE (customuser_id, group_id);


--
-- TOC entry 2264 (class 2606 OID 28130)
-- Name: users_customuser_groups users_customuser_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_customuser_groups
    ADD CONSTRAINT users_customuser_groups_pkey PRIMARY KEY (id);


--
-- TOC entry 2247 (class 2606 OID 28075)
-- Name: users_customuser users_customuser_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_customuser
    ADD CONSTRAINT users_customuser_pkey PRIMARY KEY (id);


--
-- TOC entry 2266 (class 2606 OID 28167)
-- Name: users_customuser_user_permissions users_customuser_user_pe_customuser_id_permission_7a7debf6_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_customuser_user_permissions
    ADD CONSTRAINT users_customuser_user_pe_customuser_id_permission_7a7debf6_uniq UNIQUE (customuser_id, permission_id);


--
-- TOC entry 2270 (class 2606 OID 28138)
-- Name: users_customuser_user_permissions users_customuser_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_customuser_user_permissions
    ADD CONSTRAINT users_customuser_user_permissions_pkey PRIMARY KEY (id);


--
-- TOC entry 2257 (class 2606 OID 28117)
-- Name: users_functie users_functie_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_functie
    ADD CONSTRAINT users_functie_pkey PRIMARY KEY (id);


--
-- TOC entry 2249 (class 2606 OID 28085)
-- Name: users_klantwoningbouw users_klantwoningbouw_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_klantwoningbouw
    ADD CONSTRAINT users_klantwoningbouw_pkey PRIMARY KEY (id);


--
-- TOC entry 2253 (class 2606 OID 28107)
-- Name: users_medewerkerprofile users_medewerkerprofile_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_medewerkerprofile
    ADD CONSTRAINT users_medewerkerprofile_pkey PRIMARY KEY (id);


--
-- TOC entry 2255 (class 2606 OID 28109)
-- Name: users_medewerkerprofile users_medewerkerprofile_user_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_medewerkerprofile
    ADD CONSTRAINT users_medewerkerprofile_user_id_key UNIQUE (user_id);


--
-- TOC entry 2251 (class 2606 OID 28096)
-- Name: users_role users_role_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_role
    ADD CONSTRAINT users_role_pkey PRIMARY KEY (id);


--
-- TOC entry 2231 (class 1259 OID 28067)
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- TOC entry 2236 (class 1259 OID 28063)
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- TOC entry 2239 (class 1259 OID 28064)
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- TOC entry 2226 (class 1259 OID 28049)
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- TOC entry 2271 (class 1259 OID 28202)
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- TOC entry 2274 (class 1259 OID 28203)
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- TOC entry 2334 (class 1259 OID 28516)
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- TOC entry 2337 (class 1259 OID 28515)
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- TOC entry 2298 (class 1259 OID 28297)
-- Name: mpo_bewoners_email_bewoner_67e0860a_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX mpo_bewoners_email_bewoner_67e0860a_like ON public.mpo_bewoners USING btree (email_bewoner varchar_pattern_ops);


--
-- TOC entry 2303 (class 1259 OID 28364)
-- Name: mpo_bewoners_site_id_7cde23e6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX mpo_bewoners_site_id_7cde23e6 ON public.mpo_bewoners USING btree (site_id);


--
-- TOC entry 2306 (class 1259 OID 28363)
-- Name: mpo_site_projectId_id_c37fd760; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "mpo_site_projectId_id_c37fd760" ON public.mpo_site USING btree ("projectId_id");


--
-- TOC entry 2329 (class 1259 OID 28433)
-- Name: opleverrapport_opleverrapport_author_id_2cf8d52b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX opleverrapport_opleverrapport_author_id_2cf8d52b ON public.opleverrapport_opleverrapport USING btree (author_id);


--
-- TOC entry 2332 (class 1259 OID 28434)
-- Name: opleverrapport_opleverrapport_project_id_57a1733e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX opleverrapport_opleverrapport_project_id_57a1733e ON public.opleverrapport_opleverrapport USING btree (project_id);


--
-- TOC entry 2333 (class 1259 OID 28435)
-- Name: opleverrapport_opleverrapport_site_id_5c2db7ce; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX opleverrapport_opleverrapport_site_id_5c2db7ce ON public.opleverrapport_opleverrapport USING btree (site_id);


--
-- TOC entry 2277 (class 1259 OID 28506)
-- Name: project_klantmedewerker_klantID_id_6d215918; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "project_klantmedewerker_klantID_id_6d215918" ON public.project_klantmedewerker USING btree ("klantID_id");


--
-- TOC entry 2282 (class 1259 OID 28505)
-- Name: project_project_klant_id_7a0810db; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX project_project_klant_id_7a0810db ON public.project_project USING btree (klant_id);


--
-- TOC entry 2285 (class 1259 OID 28265)
-- Name: project_project_projectnr_2fd18f33_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX project_project_projectnr_2fd18f33_like ON public.project_project USING btree (projectnr varchar_pattern_ops);


--
-- TOC entry 2290 (class 1259 OID 28504)
-- Name: project_projecticem_project_id_6c5a3aa9; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX project_projecticem_project_id_6c5a3aa9 ON public.project_projecticem USING btree (project_id);


--
-- TOC entry 2291 (class 1259 OID 28502)
-- Name: project_statusonderaanemer_onderaanemer_id_858c5606; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX project_statusonderaanemer_onderaanemer_id_858c5606 ON public.project_statusonderaanemer USING btree (onderaanemer_id);


--
-- TOC entry 2294 (class 1259 OID 28503)
-- Name: project_statusonderaanemer_project_id_id_99242435; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX project_statusonderaanemer_project_id_id_99242435 ON public.project_statusonderaanemer USING btree (project_id_id);


--
-- TOC entry 2297 (class 1259 OID 28501)
-- Name: project_vertegenwoordiger_project_vertegenwoordiger_id_dc1d8eae; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX project_vertegenwoordiger_project_vertegenwoordiger_id_dc1d8eae ON public.project_vertegenwoordiger_project USING btree (vertegenwoordiger_id);


--
-- TOC entry 2338 (class 1259 OID 28543)
-- Name: testrapport_testrapport_author_id_86dfe41d; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX testrapport_testrapport_author_id_86dfe41d ON public.testrapport_testrapport USING btree (author_id);


--
-- TOC entry 2341 (class 1259 OID 28544)
-- Name: testrapport_testrapport_project_id_c3ba7889; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX testrapport_testrapport_project_id_c3ba7889 ON public.testrapport_testrapport USING btree (project_id);


--
-- TOC entry 2342 (class 1259 OID 28545)
-- Name: testrapport_testrapport_site_id_000692ec; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX testrapport_testrapport_site_id_000692ec ON public.testrapport_testrapport USING btree (site_id);


--
-- TOC entry 2242 (class 1259 OID 28139)
-- Name: users_customuser_email_6445acef_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX users_customuser_email_6445acef_like ON public.users_customuser USING btree (email varchar_pattern_ops);


--
-- TOC entry 2245 (class 1259 OID 28151)
-- Name: users_customuser_functie_id_0d3bbe2d; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX users_customuser_functie_id_0d3bbe2d ON public.users_customuser USING btree (functie_id);


--
-- TOC entry 2259 (class 1259 OID 28164)
-- Name: users_customuser_groups_customuser_id_958147bf; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX users_customuser_groups_customuser_id_958147bf ON public.users_customuser_groups USING btree (customuser_id);


--
-- TOC entry 2262 (class 1259 OID 28165)
-- Name: users_customuser_groups_group_id_01390b14; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX users_customuser_groups_group_id_01390b14 ON public.users_customuser_groups USING btree (group_id);


--
-- TOC entry 2267 (class 1259 OID 28178)
-- Name: users_customuser_user_permissions_customuser_id_5771478b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX users_customuser_user_permissions_customuser_id_5771478b ON public.users_customuser_user_permissions USING btree (customuser_id);


--
-- TOC entry 2268 (class 1259 OID 28179)
-- Name: users_customuser_user_permissions_permission_id_baaa2f74; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX users_customuser_user_permissions_permission_id_baaa2f74 ON public.users_customuser_user_permissions USING btree (permission_id);


--
-- TOC entry 2258 (class 1259 OID 28150)
-- Name: users_functie_rol_id_b5ed4099; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX users_functie_rol_id_b5ed4099 ON public.users_functie USING btree (rol_id);


--
-- TOC entry 2345 (class 2606 OID 28058)
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2344 (class 2606 OID 28053)
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2343 (class 2606 OID 28044)
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2353 (class 2606 OID 28192)
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2354 (class 2606 OID 28197)
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_users_customuser_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_users_customuser_id FOREIGN KEY (user_id) REFERENCES public.users_customuser(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2361 (class 2606 OID 28313)
-- Name: mpo_bewoners mpo_bewoners_site_id_7cde23e6_fk_mpo_site_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mpo_bewoners
    ADD CONSTRAINT mpo_bewoners_site_id_7cde23e6_fk_mpo_site_id FOREIGN KEY (site_id) REFERENCES public.mpo_site(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2365 (class 2606 OID 28365)
-- Name: mpo_boiler mpo_boiler_icem_id_ff2ccede_fk_mpo_icem_site_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mpo_boiler
    ADD CONSTRAINT mpo_boiler_icem_id_ff2ccede_fk_mpo_icem_site_id FOREIGN KEY (icem_id) REFERENCES public.mpo_icem(site_id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2363 (class 2606 OID 28298)
-- Name: mpo_bouwkundig mpo_bouwkundig_site_id_e70f4bd4_fk_mpo_site_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mpo_bouwkundig
    ADD CONSTRAINT mpo_bouwkundig_site_id_e70f4bd4_fk_mpo_site_id FOREIGN KEY (site_id) REFERENCES public.mpo_site(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2364 (class 2606 OID 28303)
-- Name: mpo_icem mpo_icem_site_id_69e98b29_fk_mpo_site_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mpo_icem
    ADD CONSTRAINT mpo_icem_site_id_69e98b29_fk_mpo_site_id FOREIGN KEY (site_id) REFERENCES public.mpo_site(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2366 (class 2606 OID 28370)
-- Name: mpo_icemdebiet mpo_icemdebiet_icem_id_1c7cdd00_fk_mpo_icem_site_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mpo_icemdebiet
    ADD CONSTRAINT mpo_icemdebiet_icem_id_1c7cdd00_fk_mpo_icem_site_id FOREIGN KEY (icem_id) REFERENCES public.mpo_icem(site_id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2367 (class 2606 OID 28375)
-- Name: mpo_omvormer mpo_omvormer_icem_id_0d6f5238_fk_mpo_icem_site_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mpo_omvormer
    ADD CONSTRAINT mpo_omvormer_icem_id_0d6f5238_fk_mpo_icem_site_id FOREIGN KEY (icem_id) REFERENCES public.mpo_icem(site_id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2368 (class 2606 OID 28380)
-- Name: mpo_planning mpo_planning_icem_id_6f04fd35_fk_mpo_icem_site_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mpo_planning
    ADD CONSTRAINT mpo_planning_icem_id_6f04fd35_fk_mpo_icem_site_id FOREIGN KEY (icem_id) REFERENCES public.mpo_icem(site_id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2369 (class 2606 OID 28385)
-- Name: mpo_productiebonstatus mpo_productiebonstatus_icem_id_f38a996b_fk_mpo_icem_site_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mpo_productiebonstatus
    ADD CONSTRAINT mpo_productiebonstatus_icem_id_f38a996b_fk_mpo_icem_site_id FOREIGN KEY (icem_id) REFERENCES public.mpo_icem(site_id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2370 (class 2606 OID 28390)
-- Name: mpo_productieexact mpo_productieexact_icem_id_c5ac20d4_fk_mpo_icem_site_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mpo_productieexact
    ADD CONSTRAINT mpo_productieexact_icem_id_c5ac20d4_fk_mpo_icem_site_id FOREIGN KEY (icem_id) REFERENCES public.mpo_icem(site_id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2371 (class 2606 OID 28395)
-- Name: mpo_semkast mpo_semkast_icem_id_bc74ae9f_fk_mpo_icem_site_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mpo_semkast
    ADD CONSTRAINT mpo_semkast_icem_id_bc74ae9f_fk_mpo_icem_site_id FOREIGN KEY (icem_id) REFERENCES public.mpo_icem(site_id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2362 (class 2606 OID 28308)
-- Name: mpo_site mpo_site_projectId_id_c37fd760_fk_project_project_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mpo_site
    ADD CONSTRAINT "mpo_site_projectId_id_c37fd760_fk_project_project_id" FOREIGN KEY ("projectId_id") REFERENCES public.project_project(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2372 (class 2606 OID 28400)
-- Name: mpo_warmtepomp mpo_warmtepomp_icem_id_deda9ab0_fk_mpo_icem_site_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mpo_warmtepomp
    ADD CONSTRAINT mpo_warmtepomp_icem_id_deda9ab0_fk_mpo_icem_site_id FOREIGN KEY (icem_id) REFERENCES public.mpo_icem(site_id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2373 (class 2606 OID 28405)
-- Name: mpo_wtw mpo_wtw_icem_id_6d34fdb2_fk_mpo_icem_site_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mpo_wtw
    ADD CONSTRAINT mpo_wtw_icem_id_6d34fdb2_fk_mpo_icem_site_id FOREIGN KEY (icem_id) REFERENCES public.mpo_icem(site_id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2374 (class 2606 OID 28418)
-- Name: opleverrapport_opleverrapport opleverrapport_oplev_author_id_2cf8d52b_fk_users_med; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.opleverrapport_opleverrapport
    ADD CONSTRAINT opleverrapport_oplev_author_id_2cf8d52b_fk_users_med FOREIGN KEY (author_id) REFERENCES public.users_medewerkerprofile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2375 (class 2606 OID 28423)
-- Name: opleverrapport_opleverrapport opleverrapport_oplev_project_id_57a1733e_fk_project_p; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.opleverrapport_opleverrapport
    ADD CONSTRAINT opleverrapport_oplev_project_id_57a1733e_fk_project_p FOREIGN KEY (project_id) REFERENCES public.project_project(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2376 (class 2606 OID 28428)
-- Name: opleverrapport_opleverrapport opleverrapport_opleverrapport_site_id_5c2db7ce_fk_mpo_site_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.opleverrapport_opleverrapport
    ADD CONSTRAINT opleverrapport_opleverrapport_site_id_5c2db7ce_fk_mpo_site_id FOREIGN KEY (site_id) REFERENCES public.mpo_site(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2355 (class 2606 OID 28492)
-- Name: project_klantmedewerker project_klantmedewerker_klantID_id_6d215918_fk_project_klant_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.project_klantmedewerker
    ADD CONSTRAINT "project_klantmedewerker_klantID_id_6d215918_fk_project_klant_id" FOREIGN KEY ("klantID_id") REFERENCES public.project_klant(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2356 (class 2606 OID 28477)
-- Name: project_project project_project_klant_id_7a0810db_fk_project_klant_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.project_project
    ADD CONSTRAINT project_project_klant_id_7a0810db_fk_project_klant_id FOREIGN KEY (klant_id) REFERENCES public.project_klant(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2357 (class 2606 OID 28467)
-- Name: project_projecticem project_projecticem_project_id_6c5a3aa9_fk_project_project_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.project_projecticem
    ADD CONSTRAINT project_projecticem_project_id_6c5a3aa9_fk_project_project_id FOREIGN KEY (project_id) REFERENCES public.project_project(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2358 (class 2606 OID 28447)
-- Name: project_statusonderaanemer project_statusondera_onderaanemer_id_858c5606_fk_project_o; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.project_statusonderaanemer
    ADD CONSTRAINT project_statusondera_onderaanemer_id_858c5606_fk_project_o FOREIGN KEY (onderaanemer_id) REFERENCES public.project_onderaanemerbedrijf(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2359 (class 2606 OID 28457)
-- Name: project_statusonderaanemer project_statusondera_project_id_id_99242435_fk_project_p; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.project_statusonderaanemer
    ADD CONSTRAINT project_statusondera_project_id_id_99242435_fk_project_p FOREIGN KEY (project_id_id) REFERENCES public.project_project(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2360 (class 2606 OID 28437)
-- Name: project_vertegenwoordiger_project project_vertegenwoor_vertegenwoordiger_id_dc1d8eae_fk_users_med; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.project_vertegenwoordiger_project
    ADD CONSTRAINT project_vertegenwoor_vertegenwoordiger_id_dc1d8eae_fk_users_med FOREIGN KEY (vertegenwoordiger_id) REFERENCES public.users_medewerkerprofile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2377 (class 2606 OID 28528)
-- Name: testrapport_testrapport testrapport_testrapp_author_id_86dfe41d_fk_users_med; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.testrapport_testrapport
    ADD CONSTRAINT testrapport_testrapp_author_id_86dfe41d_fk_users_med FOREIGN KEY (author_id) REFERENCES public.users_medewerkerprofile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2378 (class 2606 OID 28533)
-- Name: testrapport_testrapport testrapport_testrapp_project_id_c3ba7889_fk_project_p; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.testrapport_testrapport
    ADD CONSTRAINT testrapport_testrapp_project_id_c3ba7889_fk_project_p FOREIGN KEY (project_id) REFERENCES public.project_project(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2379 (class 2606 OID 28538)
-- Name: testrapport_testrapport testrapport_testrapport_site_id_000692ec_fk_mpo_site_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.testrapport_testrapport
    ADD CONSTRAINT testrapport_testrapport_site_id_000692ec_fk_mpo_site_id FOREIGN KEY (site_id) REFERENCES public.mpo_site(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2346 (class 2606 OID 28118)
-- Name: users_customuser users_customuser_functie_id_0d3bbe2d_fk_users_functie_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_customuser
    ADD CONSTRAINT users_customuser_functie_id_0d3bbe2d_fk_users_functie_id FOREIGN KEY (functie_id) REFERENCES public.users_functie(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2349 (class 2606 OID 28154)
-- Name: users_customuser_groups users_customuser_gro_customuser_id_958147bf_fk_users_cus; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_customuser_groups
    ADD CONSTRAINT users_customuser_gro_customuser_id_958147bf_fk_users_cus FOREIGN KEY (customuser_id) REFERENCES public.users_customuser(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2350 (class 2606 OID 28159)
-- Name: users_customuser_groups users_customuser_groups_group_id_01390b14_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_customuser_groups
    ADD CONSTRAINT users_customuser_groups_group_id_01390b14_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2351 (class 2606 OID 28168)
-- Name: users_customuser_user_permissions users_customuser_use_customuser_id_5771478b_fk_users_cus; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_customuser_user_permissions
    ADD CONSTRAINT users_customuser_use_customuser_id_5771478b_fk_users_cus FOREIGN KEY (customuser_id) REFERENCES public.users_customuser(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2352 (class 2606 OID 28173)
-- Name: users_customuser_user_permissions users_customuser_use_permission_id_baaa2f74_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_customuser_user_permissions
    ADD CONSTRAINT users_customuser_use_permission_id_baaa2f74_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2348 (class 2606 OID 28145)
-- Name: users_functie users_functie_rol_id_b5ed4099_fk_users_role_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_functie
    ADD CONSTRAINT users_functie_rol_id_b5ed4099_fk_users_role_id FOREIGN KEY (rol_id) REFERENCES public.users_role(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2347 (class 2606 OID 28140)
-- Name: users_medewerkerprofile users_medewerkerprofile_user_id_dc1c9412_fk_users_customuser_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_medewerkerprofile
    ADD CONSTRAINT users_medewerkerprofile_user_id_dc1c9412_fk_users_customuser_id FOREIGN KEY (user_id) REFERENCES public.users_customuser(id) DEFERRABLE INITIALLY DEFERRED;


-- Completed on 2023-04-30 22:59:26

--
-- PostgreSQL database dump complete
--

