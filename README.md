# game-without-interface


- Oyun alanı (en az 10x10) mxm boyutlarından oluşan bir kare matristir.
- Toplam filo 1, 2, 3 ve 4 karelik (birimlik) birer gemiden oluşmaktadır.
- Gemiler oyun alanına dikey veya yatay (her gemi bağımsız olarak düşünülecek, yani bir gemi
dikey yerleşirken bir diğeri yatay olabilir) şekillerde; oyun alanının dışına çıkmayacak 
şekillerde yerleşir.
- Gemiler oyun alanına rasgele yerleştirilecektir, gemi yönleri de (dikey-yatay) rasgele
olacaktır.
- Gemiler oyun alanına yerleştirildikten sonra kullanıcıya oyun alanı 2 mod ile
gösterilebilecektir (Her iki modun sunulması zorunludur).
1- Gizli mod: Kullanıcı gemilerin nerde olduğunu bilmeyecektir.
2- Açık mod: Gemilerin yerleri oyun alanında görünecektir.
- Oyun alanında açılmayan kareler (hücreler) ? ile gösterilecektir. Karavanalar (yani yapılan
seçim boş ise bir gemi parçasını tutturamadıysa) * ile gösterilecektir. İsabetli atışların olduğu
kareler (yapılan seçim geminin bir kısmını vurdu ise) x ile gösterilecektir.
- Yapılan her atış için kullanıcıya mesaj verilecektir. Atış isabetli ise “Tebrikler bir gemi
vurdunuz”, isabetsiz ise “Maalesef isabet edemediniz” şeklinde mesajlar olacaktır. Ayrıca
isabetli bir atış yapıldığında söz konusu geminin tüm bölümleri vuruldu ise ek olarak
“Tebrikler bir gemi batırdınız” şeklinde mesaj verilecektir.
- Yapılan her atış için oyun alanının görünümü güncellenecektir (Her atıştan sonra konsol
temizlenebilir ve oyun alanının yeni hali ekrana yazdırılabilir).
- Daha önce hedef alınan bir konum seçilirse kullanıcıya başka bir konum seçmesi için bilgi
verilecektir.
- Kullanıcıya atış hakkı olarak oyun alanı büyüklüğünün 1/3’ü kadar hak verilecektir. Örnek:
10x10 (100) büyüklüğünde bir alan için atış hakkı = 100/3 = 33 olacaktır.
- Oyun iki şekilde sona erecektir. Kullanıcı tüm haklarını kullanır ve gemilerin hepsini
batıramaz. Bu durumda “Maalesef kaybettiniz” mesajı verilir. Ve ya hakları sona ermeden tüm
gemiler batırılır. Bu durumda kullanıcının puanı hesaplanır ve “Tebrikler 12 puan ile oyunu
kazandınız” şeklinde mesaj verilir. Oyun puanı toplam haktan yapılan atışlar çıkarılarak
hesaplanır.
- Oyun bittikten sonra kullanıcıya yeni oyun oynamak için veya çıkmak için tercih sunulur.
