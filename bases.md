---
layout: page
title: EFTs & bases
navigation: 2
---

# EFTs and bases

New EFTs and bases can be defined by placing the definition files into the public repository (http://github.com/wcxf/wcxf-bases). This page lists the currently defined EFTs and bases. For each basis, a PDF file listing all the operators is linked.
## EFT `SMEFT`

Standard Model Effective Field Theory with linearly realized electroweak symmetry breaking.


### Basis `Higgs-Warsaw up`

This is a mixture between the Higgs basis as defined e.g. in arXiv:1610.07922 and the Warsaw up basis. All bosonic operators involving at least one Higgs field as well as the operators of type $\psi^2 \phi^2 D$ are taken from the Higgs basis (with dimensionful Wilson coefficients rather than normalizing by $1/v^2$), while all other operators (in particular $\psi^2\phi^3$ and four-fermion operators) are defined as in the Warsaw up basis.


[List of operators (PDF)](/assets/pdf/SMEFT.Higgs-Warsaw%2520up.pdf)

### Basis `SMEFTsim-MFV`

Basis used in the `SMEFTsim_MFV` UFO models, version 3.0.0 or later. Implements Warsaw basis with $U(3)$ flavor symmetry for all fermions and includes up to 1 lepton Yukawa and 3 quark Yukawa insertions. BSM CP violation is forbidden. $q,u,d$ are the left- and right-handed quark fields. $\ell, e$ are left- and right-handed lepton fields. $Y_l,Y_u,Y_d$ are the 3x3 yukawa matrices for leptons, up- and down-quarks, defined by $L_{SM} \supset \bar d Y_d H^\dagger q$ and analogously for the others. Quark fields are in the up-aligned basis: $Y_l,Y_u$ are assumed diagonal at the scale of evaluation, while $Y_d = Y_d^{diag} V_{CKM}^\dagger$. Flavor indices are indicated with $p,r,s,t$ with Einstein conventions on repeated indices. They run over 1,2,3 for all fields. This basis definition corresponds to a fixed `LambdaSMEFT=10e+3` in the UFO models. Notation and conventions can vary compared to the Warsaw basis paper, see [arXiv:2012.11343](https://arxiv.org/abs/2012.11343) for all definitions.

[List of operators (PDF)](/assets/pdf/SMEFT.SMEFTsim-MFV.pdf)

### Basis `SMEFTsim-U35`

Basis used in the `SMEFTsim_U35` UFO models, version 3.0.0 or later. Implements Warsaw basis with $U(3)$ flavor symmetry for all fermions. For each operator, only the lowest-order flavor structure is kept. $q,u,d$ are the left- and right-handed quark fields. $\ell, e$ are left- and right-handed lepton fields. $Y_l,Y_u,Y_d$ are the 3x3 yukawa matrices for leptons, up- and down-quarks, defined by $L_{SM} \supset \bar d Y_d H^\dagger q$ and analogously for the others. Quark fields are in the up-aligned basis: $Y_l,Y_u$ are assumed diagonal at the scale of evaluation, while $Y_d = Y_d^{diag} V_{CKM}^\dagger$.  Flavor indices are indicated with $p,r,s,t$ with Einstein conventions on repeated indices. They run over 1,2,3 for all fields. This basis definition corresponds to a fixed `LambdaSMEFT=10e+3` in the UFO models.  Notation and conventions can vary compared to the Warsaw basis paper, see [arXiv:2012.11343](https://arxiv.org/abs/2012.11343) for all definitions.

[List of operators (PDF)](/assets/pdf/SMEFT.SMEFTsim-U35.pdf)

### Basis `SMEFTsim-general`

Basis used in the `SMEFTsim_general` UFO models, version 3.0.0 or later. Implements Warsaw basis with generic flavor indices for all fermions. $q,u,d$ are the left- and right-handed quark fields. $\ell, e$ are left- and right-handed lepton fields. Quark fields are in the up-aligned basis. This basis definition corresponds to a fixed `LambdaSMEFT=10e+3` in the UFO models. Notation and conventions can vary compared to the Warsaw basis paper, see [arXiv:2012.11343](https://arxiv.org/abs/2012.11343) for all definitions.

[List of operators (PDF)](/assets/pdf/SMEFT.SMEFTsim-general.pdf)

### Basis `SMEFTsim-top`

Basis used in the `SMEFTsim_top` UFO models, version 3.0.0 or later. Implements Warsaw basis with $U(2)^3$ flavor symmetry in the quarks sector and $U(1)^3$ in the leptons sector. $Q,t,b$ are left- and right-handed 3rd gen quarks, $q,u,d$ are the left- and right-handed quark fields containing only the first two generations, and transforming as $U(2)$-flavor doublets. $\ell, e$ are left- and right-handed lepton fields. $Y_u,Y_d$ are the 2x2 Yukawas of up and down quarks in the first two generations, defined by $L_{SM} \supset \bar d Y_d H^\dagger  q$ and analogously for the others. Spurions connecting the first two generations with the 3rd are absent. In the UFO models, both $Y_u$ and $Y_d$ are assumed diagonal at the scale of evaluation, and the CKM is taken to be the unit matrix. Flavor indices are indicated with $p,r,s,t$ with Einstein conventions on repeated indices. They run over 1,2 for quarks. This basis definition corresponds to a fixed `LambdaSMEFT=10e+3` in the UFO models. Notation and conventions can vary compared to the Warsaw basis paper, see [arXiv:2012.11343](https://arxiv.org/abs/2012.11343) for all definitions.

[List of operators (PDF)](/assets/pdf/SMEFT.SMEFTsim-top.pdf)

### Basis `SMEFTsim-topU3l`

Basis used in the `SMEFTsim_topU3l` UFO models, version 3.0.0 or later. Implements Warsaw basis with $U(2)^3$ flavor symmetry in the quarks sector and $U(3)^2$ in the leptons sector. $Q,t,b$ are left- and right-handed 3rd gen quarks, $q,u,d$ are the left- and right-handed quark fields containing only the first two generations, and transforming as $U(2)$-flavor doublets. $\ell, e$ are left- and right-handed lepton fields. $Y_u,Y_d$ are the 2x2 Yukawas of up and down quarks in the first two generations. $Y_l$ is the 3x3 lepton Yukawa. Yukawas defined by $L_{SM} \supset \bar d Y_d H^\dagger q$ and analogously for the others. Spurions connecting the first two generations with the 3rd are absent. In the UFO models, both $Y_u$ and $Y_d$ are assumed diagonal at the scale of evaluation, and the CKM is taken to be the unit matrix.. Flavor indices are indicated with $p,r,s,t$ with Einstein conventions on repeated indices. They run over 1,2 for quarks ans 1,2,3 for leptons. This basis definition corresponds to a fixed `LambdaSMEFT=10e+3` in the UFO models. Notation and conventions can vary compared to the Warsaw basis paper, see [arXiv:2012.11343](https://arxiv.org/abs/2012.11343) for all definitions.

[List of operators (PDF)](/assets/pdf/SMEFT.SMEFTsim-topU3l.pdf)

### Basis `Warsaw`

Basis suggested by Grzadkowski, Iskrzyński, Misiak, and Rosiek (arXiv:1008.4884v3). At variance with their definition, the Wilson coefficients are defined to be dimensionful, such that $\mathcal L=\sum _i C_i O_i$. The set of redundant operators coincides with the choice of DSixTools (arXiv:1704.04504). The weak basis for the fermion fields is chosen such that the running dimension-6 mass matrices of charged leptons and down-type quarks are diagonal at the scale where the coefficient values are specified, while up-type quark singlet field is rotated to diagonalise the running dimension-6 up-type quark mass matrix "from the right".


[List of operators (PDF)](/assets/pdf/SMEFT.Warsaw.pdf)

### Basis `Warsaw mass`

Variant of the Warsaw basis where all fermion fields are rotated such as to make their mass matrices diagonal. This rotation breaks $SU(2)_L$ invariance and is ambiguous for some operators. We adhere to the choice of arXiv:1704.03888 by Dedes, Materkowska, Paraskevas, Rosiek, and Suxho, which coincides with the "tilded" basis in arXiv:1512.02830 by Aebischer, Crivellin, Fael, and Greub.


[List of operators (PDF)](/assets/pdf/SMEFT.Warsaw%2520mass.pdf)

### Basis `Warsaw up`

Variant of the Warsaw basis where the up-type quark mass matrix (rather than the down-type quark) is diagonal.


[List of operators (PDF)](/assets/pdf/SMEFT.Warsaw%2520up.pdf)

## EFT `WET`

Weak effective theory below the electroweak scale with five dynamical quark flavours.


### Basis `Bern`

Basis suggested by Aebischer, Fael, Grueb, and Virto (arXiv:1704.06639). Neutrinos are in the flavor basis.

[List of operators (PDF)](/assets/pdf/WET.Bern.pdf)

### Basis `EOS`

Basis used by the EOS software as of version 0.4 or later. Neutrinos are in the flavour basis.

[List of operators (PDF)](/assets/pdf/WET.EOS.pdf)

### Basis `FlavorKit`

Basis used by the FlavorKit and SPheno packages

[List of operators (PDF)](/assets/pdf/WET.FlavorKit.pdf)

### Basis `JMS`

Basis suggested by Jenkins, Manohar, and Stoffer (arXiv:1709.04486). Currently only includes baryon and lepton number conserving operators. Neutrinos are in the flavour basis.

[List of operators (PDF)](/assets/pdf/WET.JMS.pdf)

### Basis `flavio`

Basis used by the flavio package. Neutrinos are in the flavour basis.

[List of operators (PDF)](/assets/pdf/WET.flavio.pdf)

### Basis `formflavor`

Basis used by the FormFlavor package

[List of operators (PDF)](/assets/pdf/WET.formflavor.pdf)

## EFT `WET-2`

Weak effective theory with dynamical up and down quark and electron, valid below the stange quark mass scale.


### Basis `JMS`

Variant of the basis suggested by Jenkins, Manohar, and Stoffer (arXiv:1709.04486) with only two dynamical quark flavors.

[List of operators (PDF)](/assets/pdf/WET-2.JMS.pdf)

## EFT `WET-3`

Weak effective theory with three dynamical quark flavours and two charged lepton flavours valid between the strange and charm quark mass scales.


### Basis `Bern`

[List of operators (PDF)](/assets/pdf/WET-3.Bern.pdf)

### Basis `JMS`

Variant of the basis suggested by Jenkins, Manohar, and Stoffer (arXiv:1709.04486) with only three dynamical quark flavors.

[List of operators (PDF)](/assets/pdf/WET-3.JMS.pdf)

### Basis `flavio`

[List of operators (PDF)](/assets/pdf/WET-3.flavio.pdf)

## EFT `WET-4`

Weak effective theory with four dynamical quark flavours valid between the charm and bottom quark mass scales.


### Basis `Bern`

[List of operators (PDF)](/assets/pdf/WET-4.Bern.pdf)

### Basis `JMS`

Variant of the basis suggested by Jenkins, Manohar, and Stoffer (arXiv:1709.04486) with only four dynamical quark flavors.

[List of operators (PDF)](/assets/pdf/WET-4.JMS.pdf)

### Basis `flavio`

[List of operators (PDF)](/assets/pdf/WET-4.flavio.pdf)

