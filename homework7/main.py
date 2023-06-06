program calc;
uses crt;
label metka;

var a,b,sum:real;
symbol1,symbol2,symbol3:char;

begin
clrscr;
writeln;
writeln('vvedite deystvie 4ere3 probel naprimer 4 - 2');

writeln;
writeln;
metka: readln(a,symbol1,symbol2,symbol3,b) ;

writeln;

case symbol2 of
'+':sum:=a+b;
'-':sum:=a-b;
'*':sum:=a*b;
'/':sum:=a/b;
else
begin
writeln('nekorrektno vvedeno deystvie, vvedite pravilno');
goto metka;
end;
end;
writeln('otvet:',sum:6:2,'.');
writeln;
writeln('************************** ********** ****************************');
readln;
end.