from usernote import app
from usernote.models import Saskaita, Asmuo, Bankas
from usernote.views import (home, asmuo_info,
                            asmuo, bankas,
                            saskaita, update_saskaita,
                            update_asmuo, update_bankas)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9050, debug=True)
