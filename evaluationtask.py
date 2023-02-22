import numpy as np

class listproblem():
  def eval_exercise1_list(input):
    """
    Silahkan masukkan dalam bentuk list.
    Seperti: [20, 30, 40, 50, 50]
    """
    try:
      if type(input) != list:
        print("Harap memasukan dalam format list diinputan")
      else:
        if input == [0, 2, 2, 3, 5, 5, 10, 10, 15, 20, 20, 20, 24, 25, 30, 40, 40, 45, 50, 77]:
          print("Urutanmu kebalik yah? yuk perbaiki")
        elif 77 not in input:
          print("Kamu sudah masukkan angka 77?")
        elif input[0] == 24:
          print("Kamu belum diurutkan yah?")
        elif input != [77, 50, 45, 40, 40, 30, 25, 24, 20, 20, 20, 15, 10, 10, 5, 5, 3, 2, 2, 0]:
          print("Jawabanmu masih ada yang salah, jangan menyerah yah!")
        else:
          print("Selamat, kamu berhasil!")
    except:
      print("Ada yang salah dari datanya")

  def eval_exercise2_list(input):
    """
    Silahkan masukkan dalam bentuk list.
    Seperti: [20, 30, 40, 50, 50]
    """
    try:
      if type(input) != list:
        print("Harap memasukan dalam format list diinputan")
      else:
        if 20 in input:
          print("Kok masih ada 20? Kan disoal lebih dari tidak sama dengan 20, bukannya?")
        elif len(input) > 3:
          print("Kamu sudah slicing belum? yuk masih ingat caranya?")
        elif input == [24, 25, 30]:
          print("Urutanmu kebalik nih? Masih ingat cara reverse?")
        elif input != [30, 25, 24]:
          print("Jawabanmu masih ada yang salah, jangan menyerah!")
        else:
          print("Selamat, kamu berhasil!")
    except:
      print("Ada yang salah dari datanya")

  answer3 = [['Pensil', 25, 2000, 0],
  ['Buku', 30, 0, 60000],
  ['Penghapus', 50, 0, 24000],
  ['Spidol', 50, 0, 100000],
  ['Sepatu', 20, 200000, 0],
  ['Kaos Kaki', 45, 10000, 0]]

  def eval_exercise3_list(input):
    """
    Silahkan masukkan dalam bentuk nested list sesuaikan dengan data yang tersedia.
    Seperti: [["Buku", 20, 0, 2000], ["Pena", 20, 0, 1000]]
    """
    try:
      if type(input) != list:
        print("Harap memasukan dalam format list diinputan")
      else:
        if input != answer3:
          print("Masih ada yang salah nih, coba guess? Pastikan dalam format nested list yah!")
        else:
          print("Selamat, kamu berhasil!")
    except: 
      print("Ada yang salah dari datanya")

  def eval_exercise4_list(input):
    """
    Silahkan masukkan dalam format tuple ([produk], total, pajak)
    Perhatikan berikut ini sebagai contoh inputan ([Buku, Tas, Spidol, Meja Tulis], 1000000, 300000)
    """
    try:
      if type(input) != tuple:
        print("Harap memasukan dalam format tuple diinputan, ketik help(eval_exercise4_list) untuk mengetahuinya")
      elif len(input) != 3:
        print("Pastikan jumlah tuplenya sesuai aturan yah")
      else:
        if input[0] == ["Buku", "Tas", "Spidol", "Meja Tulis", "Papan Tulis", "Lemari", "Kursi", "Sepatu", "Kaos Kaki"]:
          print("Produk item sudah benar")
          if input[1] == 2160000:
            print("Total semua item sudah benar")
            if input[2] == 237600:
              print("Pajaknya sudah benar")
            else:
              print("Pajak masih salah yah!")
          else:
            print("Total semua item salah yah!")
            if input[2] == 237600:
              print("Pajaknya sudah benar")
            else:
              print("Pajak masih salah yah!")
        else:
          print("Produk item masih salah yah!")
          if input[1] == 2160000:
            print("Total semua item sudah benar")
            if input[2] == 237600:
              print("Pajaknya sudah benar")
            else:
              print("Pajak masih salah yah!")
          else:
            print("Total semua item salah yah!")
            if input[2] == 237600:
              print("Pajaknya sudah benar")
            else:
              print("Pajak masih salah yah!")
    except: 
      print("Ada yang salah dari datanya")

  def eval_exercise5_list(input):
    """
    Silahkan masukkan dalam format tuple (rata-rata, total angka 20, [list tanpa duplikasi])
    Perhatikan berikut ini sebagai contoh inputan (10, 23, [0, 2, 3])
    """
    try:
      if type(input) != tuple:
        print("Harap memasukan dalam format tuple diinputan, ketik help(eval_exercise4_list) untuk mengetahuinya")
      elif len(input) != 3:
        print("Pastikan jumlah tuplenya sesuai aturan yah")
      else:
        if np.ceil(input[0]) == 33:
          print("Rata-ratanya sudah sesuai")
          if input[1] == 3:
            print("Jumlah item 20 sudah sesuai")
            if input[2] == [0, 10, 20, 30, 40, 50, 60, 80]:
              print("Item tanpa duplikasi sudah sesuai")
            else:
              print("Item tanpa duplikasi belum sesuai")
          else:
            print("Jumlah item 20 belum sesuai")
            if input[2] == [0, 10, 20, 30, 40, 50, 60, 80]:
              print("Item tanpa duplikasi sudah sesuai")
            else:
              print("Item tanpa duplikasi belum sesuai")
        else:
          print("Rata-ratamu masih salah nih")
          if input[1] == 3:
            print("Jumlah item 20 sudah sesuai")
            if input[2] == [0, 10, 20, 30, 40, 50, 60, 80]:
              print("Item tanpa duplikasi sudah sesuai")
            else:
              print("Item tanpa duplikasi belum sesuai")
          else:
            print("Jumlah item 20 belum sesuai")
            if input[2] == [0, 10, 20, 30, 40, 50, 60, 80]:
              print("Item tanpa duplikasi sudah sesuai")
            else:
              print("Item tanpa duplikasi belum sesuai")
    except: 
      print("Ada yang salah dari datanya")