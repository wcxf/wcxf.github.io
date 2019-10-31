from wilson import wcxf
import subprocess
from urllib.parse import quote

for name, basis in wcxf.Basis.instances.items():
    fname = '.'.join([quote(n) for n in name])
    subprocess.run(['pandoc', '-t', 'latex',
                    '-o', 'assets/pdf/{}.pdf'.format(fname)],
                   input=str(basis).encode())

with open('_bases.md', 'r') as f:
    bases_header = f.read()

with open('bases.md', 'w') as f:
    f.write(bases_header)
    for eftname in sorted(wcxf.EFT.instances):
        eft = wcxf.EFT[eftname]
        f.write("## EFT `{}`\n\n".format(eft.eft))
        if hasattr(eft, 'metadata') and 'description' in eft.metadata:
            f.write(eft.metadata['description'] + "\n\n")
        bases = eft.known_bases
        for bname in bases:
            basis = wcxf.Basis[eft.eft, bname]
            f.write("### Basis `{}`\n\n".format(basis.basis))
            if hasattr(basis, 'metadata') and 'description' in basis.metadata:
                f.write(basis.metadata['description'] + "\n\n")
            fname = '.'.join([quote(quote(n)) for n in [eft.eft, bname]])
            f.write("[List of operators (PDF)](/assets/pdf/{}.pdf)\n\n".format(fname))
