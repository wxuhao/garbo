#MaxThreadsPerHotkey 2

F2::
CoordMode Mouse, Screen
Toggle := !Toggle
loop
{
	If not Toggle
		break
	sleep 300
	Send, {Enter}
	sleep 300
	Send, /surrender
	sleep 300
	Send, {Enter}
	sleep 300
	Click, 1360, 665
	sleep 300
	Click, 1180, 1025
	sleep 300
	Click, 1455, 400
	sleep 300
	Click, 1280, 900
}
return
F3::
MouseGetPos, xpos, ypos 
MsgBox, The cursor is at X%xpos% Y%ypos%.
return