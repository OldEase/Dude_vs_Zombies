# Dude_vs_Zombies
Цуркан-Тарасов-Чикалкин

Проект представляет собой компьютерную игру на одного
игрока. Для удобства читателя описание игры 
разбито на два блока: 
для игрока и для программиста.

Блок 1. (для игрока)
Запустить игру просто - нужно всего лишь открыть 
файл main_file.py. Правда, перед этим рекомендуем 
ознакомиться с правилами и особенностями игры.
1. Игровой сюжет.
   Представьте, что Вы проезжаете опасный участок 
   дороги, про который давно ходят недобрые слухи.
   Вы уже почти миновали опасное место, но - вот
   незадача! - у Вас сломалась машина. Быстрее чините
   ее, пока коварные зомби не уничтожили Вас. 
   Если сможете отбиться от монстров, починить
   машину и уехать - Вы победили. 
   Иначе - не повезло...
2. Управление игрой.
   2.1. Движение. 
     Ваш герой может перемещаться по игровому 
     полю. Для движения влево/вправо нажмите
     и удерживайте клавиши left_arrow/right_arrow
     на клавиатуре, для прыжка - up_arrow. 
     Перепрыгивайте через зомби - так Вы можете
     избежать урона, который они наносят при каждом 
     столкновении с Вами. Учтите, что Ваш герой 
     не может выбежать за пределы игрового поля, 
     поэтому загнать героя на край площадки -
     не лучшее решение.
   2.2. Стрельба.
   Хорошо, что у Вас есть возможность отстреливаться
     от зомби. Для этого у Вас есть арсенал оружия
     (правда, изначально (до покупок в магазине) в нем
     только пистолет, но и это лучше, чем ничего).
     Нажимая кнопки 1 - 5 на клавиатуре, можете 
     экспериментировать, меняя свое активное оружие
     на какое-то другое из своего арсенала. Если
     у Вас нет данного вида оружия (1 - PISTOL, 
     2 - REVOLVER, 3 -  WINCHESTER, 4 - UZI, 
     5 - MOSSBERG), то при нажатии соответствующей
     клавиши в руках у героя окажется пистолет. Учтите - 
     разное оружие имеет разные характеристики
     (скорость перезарядки, наносимый урон). 
     Целиться по врагу просто - наведите джойстик
     на нужное место экрана. Щелчком мыши Вы
     даете своему герою команду сделать выстрел.
     При достаточно меткой стрельбе Вы можете 
     таться и монстров убивать, и машину успевать
     чинить.
   2.3. Кстати, о машине. Чтобы начать ее ремонтировать
   (надо же как-то выбираться из этой заварушки!), 
   запрыгните на нее и нажмите down_arrow на
    клавиатуре. Учтите - пока Вы заняты ремонтом
    машины, от всего другого придется отвлечься - 
    Вы не можете параллельно делать покупки в магазине, стрелять
    и т.п. Кроме того, пока Вы на машине, зомби не
    могут Вас достать. Но не думайте, что это Вам
    просто так сойдет с рук - разъяренные монстры начнут
    добивать Вашу несчастную машину, ее уровень
    починки будет стремительно падать, и чинить ее
    станет намного труднее. Если же уровень починки
    упадет до 0 (машина окончательно сломается), Ванему герою
    не суждено выбраться из этого страшного места, 
    поэтому придется начинать игру сначала. Поэтому
    будбте внимательны и следите за уровнем починки
    - он отображается снизу под машиной (кстати, 
   над каждым монстром Вы можете увидеть его 
   оставшееся здоровье, а вверху экрана отображается
   уровень здоровья Вашего героя). Если же
   уровень починки машины достигнет необходимого
   значения - Вы выбрались из этого логова монстров, 
   что означает победу.
   2.4. Магазин.
     За каждого убитого монстра герою начисляются
   деньги. Тратить их можно (и нужно!) в магазине в любой 
   момент игры. На них Вы можете купить более
   совершенное оружие (см. выше) или аптечку, которая
   повысит здоровье героя. Для покупки достаточно
   нажать на цену выбранного Вами товара.
   2.5. Личные навыки
   Во время сражений с монстрами герой набирается
   опыта, что увеличивает со временем его некоторые
   параметры. Так что сражайтесь с монстрами, а не
   бегайте от них (если только не пришлось
   совсем туго)!
   Вот, собственно, и все правила. Удачи!
3. Блок 2 (для программиста)
   Возможно, некоторые из игроков не удовлетворятся
   представленным вариантом игры, захотят его
   облегчить, усложнить или видоизменить. Это возможно,
   и мы хотим помочь им в этом,описав основные моменты
   работы программы.
Программа разбита на следующие модули:
  1) main_file.py - главный модуль, осуществляет
общее управление работой программы, импортирует все
остальные модули;
  2) Functions.py - здесь собрано большинство
используемых в программе функций;
  3) Classes.py - представлено большинство
используемых в программе классов (кроме классов
монстров и оружия)
  4) Zombies_class.py - собраны классы монстров;
  5) Gun_class.py - классы оружия;
  6) Surfaces.py - собраны поверхности с нарисованными
     графическими объектами;
  7) Special_functions