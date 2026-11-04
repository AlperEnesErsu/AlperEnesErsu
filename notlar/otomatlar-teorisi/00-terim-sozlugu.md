# 0 · Terim Sözlüğü (TR – EN)

Derslerin kaynağı İngilizce, sınav Türkçe olabilir. İki dildeki karşılıkları bir arada.

| Türkçe | İngilizce | Kısa açıklama |
| --- | --- | --- |
| Otomat / otomatlar | automaton / automata | Hesaplama modeli |
| Alfabe | alphabet (Σ) | Sonlu sembol kümesi |
| Dizgi | string | Sembollerin sonlu dizisi |
| Boş dizgi | empty string (ε) | Uzunluğu 0 olan dizgi |
| Dil | language | Dizgilerden oluşan küme |
| Belirlenimli sonlu otomat | deterministic finite automaton (DFA) | Her durum ve sembol için tam bir geçiş |
| Belirlenimsiz sonlu otomat | nondeterministic finite automaton (NFA) | Birden fazla, hiç ya da ε geçişi olabilir |
| Geçiş fonksiyonu | transition function (δ) | Durum + sembol → durum |
| Başlangıç durumu | start state (q0) | Diyagramda dışarıdan gelen ok |
| Kabul durumu | accept / final state (F) | Diyagramda çift çember |
| Tuzak durumu | trap / dead / sink state | Çıkışı olmayan ret durumu |
| Tanımak | recognize | Makinenin dili tam olarak kabul etmesi |
| Düzenli dil | regular language | Bir sonlu otomatın tanıdığı dil |
| Düzenli ifade | regular expression | `∪`, birleştirme ve `*` ile kurulan ifade |
| Birleşim | union (∪) | İki dilin dizgilerinin tümü |
| Birleştirme / ekleme | concatenation (∘) | Bir dizginin arkasına diğerini eklemek |
| Yıldız işlemi | Kleene star (*) | Sıfır ya da daha fazla tekrar |
| Kapanış | closure | İşlem sonucunun yine aynı sınıfta kalması |
| Alt küme yapısı | subset construction | NFA → DFA dönüşümü |
| ε-kapanışı | ε-closure | ε ile ulaşılabilen durumlar |
| Genelleştirilmiş NFA | generalized NFA (GNFA) | Oklarında ifade yazan NFA |
| Pompalama önsavı | pumping lemma | Düzenli olmamayı gösterme aracı |
| Pompalama uzunluğu | pumping length (p) | Önsavdaki eşik uzunluk |
| Güvercin yuvası ilkesi | pigeonhole principle | Önsavın dayandığı sayma ilkesi |
| Durum küçültme | DFA minimization | Eşdeğer durumları birleştirme |

## Gösterim hatırlatmaları

- `Σ*`: Σ üzerindeki tüm dizgiler (ε dahil).
- `Σ⁺ = ΣΣ*`: en az bir sembollü dizgiler.
- `|w|`: w'nin uzunluğu. `wᴿ`: w'nin tersi.
- `L(M)`: M makinesinin tanıdığı dil.
