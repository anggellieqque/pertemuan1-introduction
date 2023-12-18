sasuke_perkenalan = 'Hallo.. Nama saya sasuke, saya berusia 17 tahun'
print(sasuke_perkenalan)

sasuke_perkenalan = sasuke_perkenalan.split(" ")
print(sasuke_perkenalan)
print(f"index-6: {sasuke_perkenalan[6]}")
print(f"type index-6: {type(sasuke_perkenalan[6])}")

sasuke_perkenalan[6] = int(sasuke_perkenalan[6])
print(sasuke_perkenalan)
print(f"index-6: {sasuke_perkenalan[6]}")
print(f"type index-6: {type(sasuke_perkenalan[6])}")