BEGIN;

    CREATE TABLE core_category
    (
      slug      VARCHAR(50)  NOT NULL
        CONSTRAINT core_category_pkey
        PRIMARY KEY,
      name      VARCHAR(255) NOT NULL,
      lft       INTEGER      NOT NULL
        CONSTRAINT core_category_lft_check
        CHECK (lft >= 0),
      rght      INTEGER      NOT NULL
        CONSTRAINT core_category_rght_check
        CHECK (rght >= 0),
      tree_id   INTEGER      NOT NULL
        CONSTRAINT core_category_tree_id_check
        CHECK (tree_id >= 0),
      level     INTEGER      NOT NULL
        CONSTRAINT core_category_level_check
        CHECK (level >= 0),
      parent_id VARCHAR(50)
        CONSTRAINT core_category_parent_id_f82a0951_fk_core_category_slug
        REFERENCES core_category
          DEFERRABLE INITIALLY DEFERRED
    );
    CREATE INDEX core_category_slug_384eca9c_like
      ON core_category (slug);
    CREATE INDEX core_category_lft_9a1c6363
      ON core_category (lft);
    CREATE INDEX core_category_rght_84984554
      ON core_category (rght);
    CREATE INDEX core_category_tree_id_1d1aaa95
      ON core_category (tree_id);
    CREATE INDEX core_category_level_46282c5a
      ON core_category (level);
    CREATE INDEX core_category_parent_id_f82a0951
      ON core_category (parent_id);
    CREATE INDEX core_category_parent_id_f82a0951_like
      ON core_category (parent_id);

    CREATE TABLE core_author
    (
      slug VARCHAR(50)  NOT NULL
        CONSTRAINT core_author_pkey
        PRIMARY KEY,
      name VARCHAR(255) NOT NULL
    );
    CREATE INDEX core_author_slug_3da241de_like
      ON core_author (slug);

    CREATE TABLE core_language
    (
      slug VARCHAR(50)  NOT NULL
        CONSTRAINT core_language_pkey
        PRIMARY KEY,
      name VARCHAR(150) NOT NULL
    );
    CREATE INDEX core_language_slug_09b02269_like
      ON core_language (slug);

    CREATE TABLE core_publisher
    (
      slug VARCHAR(50)  NOT NULL
        CONSTRAINT core_publisher_pkey
        PRIMARY KEY,
      name VARCHAR(150) NOT NULL
    );
    CREATE INDEX core_publisher_slug_36308bcd_like
      ON core_publisher (slug);

    CREATE TABLE core_type
    (
      slug VARCHAR(50) NOT NULL
        CONSTRAINT core_type_pkey
        PRIMARY KEY,
      name VARCHAR(50) NOT NULL
    );
    CREATE INDEX core_type_slug_c8a95a36_like
      ON core_type (slug);

    CREATE TABLE core_book
    (
      created_date      TIMESTAMP WITH TIME ZONE NOT NULL,
      id                SERIAL                   NOT NULL
        CONSTRAINT core_book_pkey
        PRIMARY KEY,
      slug              VARCHAR(50)              NOT NULL UNIQUE,
      name              VARCHAR(255)             NOT NULL,
      format            VARCHAR(100),
      pages             INTEGER                  NOT NULL,
      year              INTEGER                  NOT NULL,
      cover             VARCHAR(100)             NOT NULL,
      weight            INTEGER                  NOT NULL,
      description_big   TEXT                     NOT NULL,
      description_small TEXT                     NOT NULL,
      category_id       VARCHAR(50)              NOT NULL
        CONSTRAINT core_book_category_id_cea0e710_fk_core_category_slug
        REFERENCES core_category
          DEFERRABLE INITIALLY DEFERRED,
      language_id       VARCHAR(50)              NOT NULL
        CONSTRAINT core_book_language_id_c81361ae_fk_core_language_slug
        REFERENCES core_language
          DEFERRABLE INITIALLY DEFERRED,
      publisher_id      VARCHAR(50)              NOT NULL
        CONSTRAINT core_book_publisher_id_b9885380_fk_core_publisher_slug
        REFERENCES core_publisher
          DEFERRABLE INITIALLY DEFERRED,
      type_id           VARCHAR(50)
        CONSTRAINT core_book_type_id_ec284f44_fk_core_type_slug
        REFERENCES core_type
          DEFERRABLE INITIALLY DEFERRED,
      isbn              VARCHAR(25)              NOT NULL,
      isbn2             VARCHAR(25),
      origin_name       VARCHAR(255),
      series            VARCHAR(255),
      paper_url         VARCHAR(255),
      paper_name        VARCHAR(100),
      content           TEXT                     NOT NULL
    );
    CREATE INDEX core_book_slug_d62cdd35
      ON core_book (slug);
    CREATE INDEX core_book_slug_d62cdd35_like
      ON core_book (slug);
    CREATE INDEX core_book_category_id_cea0e710
      ON core_book (category_id);
    CREATE INDEX core_book_category_id_cea0e710_like
      ON core_book (category_id);
    CREATE INDEX core_book_language_id_c81361ae
      ON core_book (language_id);
    CREATE INDEX core_book_language_id_c81361ae_like
      ON core_book (language_id);
    CREATE INDEX core_book_publisher_id_b9885380
      ON core_book (publisher_id);
    CREATE INDEX core_book_publisher_id_b9885380_like
      ON core_book (publisher_id);
    CREATE INDEX core_book_type_id_ec284f44
      ON core_book (type_id);
    CREATE INDEX core_book_type_id_ec284f44_like
      ON core_book (type_id);

    CREATE TABLE core_book_author
    (
      id        SERIAL      NOT NULL
        CONSTRAINT core_book_author_pkey
        PRIMARY KEY,
      book_id   INTEGER     NOT NULL
        CONSTRAINT core_book_author_book_id_bc90460a_fk_core_book_id
        REFERENCES core_book
          DEFERRABLE INITIALLY DEFERRED,
      author_id VARCHAR(50) NOT NULL
        CONSTRAINT core_book_author_author_id_ada6e686_fk_core_author_slug
        REFERENCES core_author
          DEFERRABLE INITIALLY DEFERRED,
      CONSTRAINT core_book_author_book_id_author_id_551c1494_uniq
      UNIQUE (book_id, author_id)
    );
    CREATE INDEX core_book_author_book_id_bc90460a
      ON core_book_author (book_id);
    CREATE INDEX core_book_author_author_id_ada6e686
      ON core_book_author (author_id);
    CREATE INDEX core_book_author_author_id_ada6e686_like
      ON core_book_author (author_id);

    CREATE TABLE version_version
    (
      id      SERIAL      NOT NULL
        CONSTRAINT version_version_pkey
        PRIMARY KEY,
      version VARCHAR(25) NOT NULL
    );

COMMIT;