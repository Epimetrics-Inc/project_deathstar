```
sudo apt-get install postgresql-server-dev-9.5

sudo apt-get install postgresql-contrib-9.5

git clone https://github.com/michelp/pgjwt.git
cd pgjwt
sudo make install

psql -f initdb.sql -d dev <or what the dbname should be>
psql -d dev -f populate.bak -Fc -v ON_ERROR_STOP=1 -d dev <or what the dbname should be>
```