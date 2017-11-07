
sudo apt-get install postgresql-server-dev-9.5
sudo apt-get install postgresql-contrib-9.5

git clone https://github.com/michelp/pgjwt.git
cd pgjwt
make install

psql -f initdb.sql -d dev
psql -d dev -f populate.bak -Fc -v ON_ERROR_STOP=1
