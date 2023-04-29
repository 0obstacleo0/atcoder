n = int(input())
s = input()

start = s.find("|")
end = s.rfind("|")
if start <= s.find("*") and s.find("*") <= end:
    print("in")
else:
    print("out")
