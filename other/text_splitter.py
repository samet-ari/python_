text = "Lorem ipsum dolor sit amet, consectetur adipiscing\
elit. Etiam interdum massa non nisl venenatis, in finibus\
lectus fermentum. Maecenas quis imperdiet ligula. Phasellus\
non laoreet arcu. Mauris tristique commodo ipsum vel fermentum.\
Ut ut auctor diam. Nulla vel porta lorem, in scelerisque justo.\
Suspendisse facilisis mollis arcu non eleifend. Donec lacinia\
elit vel leo fermentum, a condimentum ex fermentum. Nam non\
augue quis leo mollis ultrices non fermentum nibh. Sed egestas\
venenatis velit pulvinar rhoncus. Vivamus feugiat orci\
porttitor, placerat lorem vel, sodales nunc. Phasellus\
sed ornare ipsum. Aliquam sed sem vitae sem dictum semper sed\
a lectus. Pellentesque non commodo nunc. Cras at egestas enim,\
rhoncus pretium diam. Donec varius, odio id fermentum dignissim,\
orci dui finibus urna, in aliquam urna ligula at nunc. Proin\
laoreet tristique tincidunt. Aliquam viverra quam erat, eget\
cursus mauris posuere ac. Sed commodo efficitur leo, scelerisque\
volutpat justo cursus id. Donec dictum gravida purus quis vulputate.\
Nunc rutrum scelerisque aliquam. Cras commodo ornare porttitor.\
Aenean eget eros et tortor placerat pellentesque. Morbi lobortis\
magna quis pellentesque finibus. Integer massa eros, congue quis\
aliquam sed, cursus id ligula. Suspendisse vitae lectus mauris.Mauris\
venenatis urna in consectetur ullamcorper. Donec pellentesque ac massa\
nec mollis. Quisque tempus dui id dolor fermentum dapibus. Fusce at mollis\
leo. Nunc vitae nunc in sapien consequat posuere. Ut quis euismod nibh.\
Ut commodo tempus lorem at auctor. Sed fermentum mauris libero,\
at euismod sem posuere ut. Vestibulum rutrum felis sapien, quis\
gravida ex porta at. Proin viverra dolor at leo tempor, vitae\
ornare nisl faucibus. Mauris vestibulum, diam eget aliquet\
sodales, est augue tempus eros, in iaculis\
sapien urna sed ante."
symbols = 300

es = [text[i : i + symbols] for i in range(0, len(text), symbols)]
for n in es:
    print(n + "\n\n")
