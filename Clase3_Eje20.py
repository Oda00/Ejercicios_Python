
A=["hola","gato","perro","negro","palabra","texto","contexto","gato","hola"]
print(A)

for i in range ((len(A)-1),-1,-1):
    if A[i]in A[:i]:
        del(A[i])
print(A)
