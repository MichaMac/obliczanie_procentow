import streamlit as st

# Tytuł aplikacji
st.title("Obliczanie procentowego udziału czasu na zadania")

# Wprowadzenie liczby godzin z umowy
godziny_umowy = st.number_input("Wpisz ilość godzin z umowy:", min_value=0, step=1)
minuty_umowy = godziny_umowy * 60

# Komunikat dla użytkownika
st.write("W kolejnych polach wpisz po przecinku ilość czasu w minutach, które przeznaczone były na zadania np. 240,240,240 itd.")

# Zadania oraz ich czasy w minutach
zadania = {
    'Egzaminy (nagrywane i nienagrywane)': [],
    'Checker': [],
    'Redakcja': [],
    'QB': [],
    'Kawki zespołowe': [],
    'Kawki przedmiotowe': [],
    'Chmurowe spotkania: ogólne szkolenia/ ogólne spotkania': [],
    'Inne (wiadomości chmurkowe etc.)': []
}

# Tworzenie pól do wprowadzania czasów
suma_minut = {}
for zadanie in zadania.keys():
    czasy = st.text_input(zadanie, "")
    zadania[zadanie] = list(map(int, czasy.split(','))) if czasy else []

# Obliczenie sumy minut dla każdego zadania
suma_minut = {zadanie: sum(czasy) for zadanie, czasy in zadania.items()}

# Całkowita liczba minut
calosc_minuty = sum(suma_minut.values())

# Obliczenie procentowego udziału dla każdego zadania
procenty = {zadanie: (czas / calosc_minuty) * 100 if calosc_minuty > 0 else 0 for zadanie, czas in suma_minut.items()}

# Wyświetlenie wyników
st.write("Całkowita liczba godzin wprowadzona: ", godziny_umowy, " godzin")
st.write("Całkowita liczba minut na zadania: ", calosc_minuty, " minut")

# Tabela wyników w procentach
st.subheader("Procentowy udział czasu na poszczególne zadania:")
for zadanie, procent in procenty.items():
    st.write(f"{zadanie}: {procent:.2f}%")
