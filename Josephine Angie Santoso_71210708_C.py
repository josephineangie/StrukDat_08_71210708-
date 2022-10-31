class NodePelanggan:
    def __init__(self, namaPelanggan):
        self._namaPelanggan = namaPelanggan

    def getNamaPelanggan(self):
        return self._namaPelanggan

    def setnamaPelanggan(self, namaPelangganBaru):
        self._namaPelanggan = namaPelangganBaru


# class Node:
#     def __init__(self, element, next):
#         self._element = element
#         self._next = next


class Kasir:
    DEFAULT_CAPACITY = 3

    def __init__(self):  # konstruktor
        # pass
        # self._head = None
        # self._tail = None
        # self._size = 0
        self._data = []
        self._default = Kasir.DEFAULT_CAPACITY

    def __len__(self):  # mengembalikan ukuran Queue
        # pass
        # return self._size
        return len(self._data)

    def is_empty(self):  # mengecek apakah Queue kosong ?
        # pass
        # return self._size == 0
        return len(self._data) == 0

    def dequeue(self):  # menghapus data paling depan (front)
        # pass
        # if self.is_empty() == False:
        #     value = self._head._element
        #     if self._size == 1:
        #         self._head = None
        #         self._tail = None
        #     else:
        #         hapus = self._head
        #         self._head = self._head._next
        #         del hapus
        #     self._size -= 1
        #     return value
        # else:
        #     return None
        data = self._data[0]
        self._data.remove(data)
        print("### Pelanggan {data} Selesai Membayar ###")
        print()

    def enqueue(self, namaPelanggan):  # menambah data ke list
        # pass
        # baru = Node(namaPelanggan, None)
        # if self.is_empty():
        #     self._head = baru
        #     self._tail = baru
        # else:
        #     self._tail._next = baru
        #     self._tail = baru
        # self._size += 1
        self._data.append(namaPelanggan)

    def resize(self, cap):  # mengubah ukuran queue pada list
        print("### Melakukan Resize ###")
        print()
        self._default = self._default * cap

    def printAll(self):  # menampilkan daftar pelanggan dalam sebuah kasir
        # pass
        # bantu = self._head
        # while bantu != None:
        #     print(bantu._element, end=' ')
        #     bantu = bantu._next
        #     print()
        # for i in range(0, len(self._data)):
        #     print(self._data[i], end=' ')
        print("=== Kasir ===")
        if len(self._data) > self._default:
            self.resize(2)
        c = len(self._data)-1
        n = 1
        for i in range(0, (self._default)):
            if i <= c:
                print(n, ".", self._data[i], end=" ")
                print()
            else:
                print(n, ". Kosong")
            n += 1
        print()


# test case program
tempatKasir = Kasir()
tempatKasir.enqueue("Haniif")
tempatKasir.enqueue("Sindu")
tempatKasir.enqueue("Dedi")
tempatKasir.printAll()

tempatKasir.enqueue("Beatrix")
tempatKasir.printAll()

tempatKasir.dequeue()
tempatKasir.printAll()

tempatKasir.enqueue("Shalom")
tempatKasir.printAll()

tempatKasir.dequeue()
tempatKasir.printAll()
