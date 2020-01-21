namespace :setup do
  desc "Tracker installation has started"
  task :start do
    system %{
      pip install -r requirements.txt
      dropdb -i tracker &&
      createdb -E UTF8 -T template0 --lc-collate=tr_TR.UTF-8 --lc-ctype=tr_TR.UTF-8 tracker &&
      python manage.py migrate
      echo "tracker installation ended..."
    }
  end
end