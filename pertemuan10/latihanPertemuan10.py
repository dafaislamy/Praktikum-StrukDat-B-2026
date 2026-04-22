'''
Skenario: Bayangkan Anda adalah seorang Software Engineer yang ditugaskan
untuk membuat sistem "Riwayat Navigasi" (Browser History) sederhana. Setiap kali
pengguna mengunjungi halaman web baru, URL halaman tersebut akan ditumpuk.
Jika pengguna menekan tombol "Back", halaman terakhir akan dihapus dari riwayat
dan pengguna kembali ke halaman sebelumnya.
Sistem ini sangat cocok menggunakan struktur data Stack (LIFO - Last In First
Out).

Tugas Anda: Anda diminta untuk mengimplementasikan sistem ini menggunakan
dua cara yang berbeda:
1. Menggunakan List biasa (Dynamic Array) bawaan Python.
2. Menggunakan Linked List.
Kedua implementasi tersebut wajib memiliki 5 operasi dasar Stack berikut:
1. is_empty(): Memeriksa apakah riwayat kosong (mengembalikan True atau
False).
2. push(url): Menambahkan URL baru ke posisi teratas (pengguna membuka
halaman baru).
3. pop(): Menghapus dan mengembalikan URL di posisi teratas (pengguna
menekan tombol 'Back'). Jika kosong, kembalikan teks "Riwayat kosong".
4. peek(): Melihat URL yang ada di posisi teratas tanpa menghapusnya (melihat
halaman yang sedang aktif). Jika kosong, kembalikan None.
5. size(): Menghitung total URL yang tersimpan di dalam riwayat saat ini.
'''

#Bagian 1 - Implementasi Menggunakan List Biasa
class StackList:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, url):
        self.stack.append(url)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]

    def size(self):
        return len(self.stack)

stack_list = StackList()

stack_list.push("www.google.com")
stack_list.push("www.instagram.com")

print(stack_list.stack)
print(stack_list.pop())
print(stack_list.peek())
print(stack_list.size())
print()


#Bagian 2 - Implementasi Menggunakan Linked List
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def push(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.value

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.head.value

    def Size(self):
        return self.size
  
stack_linked_list = StackLinkedList()

stack_linked_list.push("www.facebook.com")
stack_linked_list.push("www.youtube..com")

print(stack_linked_list.pop())
print(stack_linked_list.peek())
print(stack_linked_list.Size())