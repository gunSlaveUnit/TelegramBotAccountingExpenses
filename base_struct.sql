create table categories(
    id serial,
    name varchar(50) primary key,
    is_income boolean,
    aliases text
);

create table expenses(
    id serial,
    amount integer,
    created date,
    category_name varchar(50),
    clarification text,
    FOREIGN KEY(category_name) REFERENCES categories(name)
);

insert into categories (name, is_income, aliases)
values
    ('products', false, 'food'),
    ('transport',  false, 'autobus, metro, taxi'),
    ('phone', false, 'telephone, smartphone'),
    ('books', false, 'literature'),
    ('internet', false, 'inet'),
    ('subscriptions', false, 'services'),
    ('other', false, 'something');