# python program implementering af Bubble Sort

#Python Essentials 2, lab 6.3.2

def bubbleSort(arr):
    n = len(arr)

    # Optimering: Hvis Array allerede  er sorteret behøver vi ikke at gennemgå hele processen   igen
    # Gå  igennem alle  elementerne i Array

    for i in range(n-1):

        # køre en gang mere end nødvendigt.
        # de sidste i elemente er allerede sorteret

        swapped = False
        for j in range(0, n-i-1):

            #  gå igennem  arrayet fra 0 til n-i-1
             # Byt, hvis element er større end det næste  element
            
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:

         # hvis  vi ikke har byttet nogle elementer kan afslutte Loop
            return

# Test array
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print("% d" % arr[i], end=" ")

