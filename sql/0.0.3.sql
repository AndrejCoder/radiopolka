begin;
    insert into core_publisher values ('W', 'W');
    update core_book set publisher_id = 'W' where publisher_id = 'Wiliams';
    update core_publisher set slug = 'wiliams' where slug = 'Wiliams';
    update core_book set publisher_id = 'wiliams' where publisher_id = 'W';
    delete from core_publisher where slug = 'W';

    insert into core_publisher values ('S', 'S');
    update core_book set publisher_id = 'S' where publisher_id = 'Stolichnaya-Enciklopediya';
    update core_publisher set slug = 'stolichnaya-enciklopediya' where slug = 'Stolichnaya-Enciklopediya';
    update core_book set publisher_id = 'stolichnaya-enciklopediya' where publisher_id = 'S';
    delete from core_publisher where slug = 'S';
commit;