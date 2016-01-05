# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

OPERACION_SUJETA_Y_EXENTA = '01'
OPERACION_NO_SUJETA = '02'
ZIP = 'ZIP'
GZIP = 'GZIP'
NONE = 'NONE'
XML = 'xml'
DOC = 'doc'
GIF = 'gif'
RTF = 'rtf'
PDF = 'pdf'
XLS = 'xls'
JPG = 'jpg'
BMP = 'bmp'
TIFF = 'tiff'
BASE = 'BASE64'
BER = 'BER'
DER = 'DER'
PERSONA_FISICA = 'F'
PERSONA_JURIDICA = 'J'
EXTRANJERO = 'E'
RESIDENTE = 'R'
RESIDENTE_EN_LA_UNION_EUROPEA = 'U'
AFG = 'AFG'
ALB = 'ALB'
DZA = 'DZA'
ASM = 'ASM'
AND = 'AND'
AGO = 'AGO'
AIA = 'AIA'
ATG = 'ATG'
ARG = 'ARG'
ARM = 'ARM'
ABW = 'ABW'
AUS = 'AUS'
AUT = 'AUT'
AZE = 'AZE'
BHS = 'BHS'
BHR = 'BHR'
BGD = 'BGD'
BRB = 'BRB'
BLR = 'BLR'
BEL = 'BEL'
BLZ = 'BLZ'
BEN = 'BEN'
BMU = 'BMU'
BTN = 'BTN'
BOL = 'BOL'
BIH = 'BIH'
BWA = 'BWA'
BRA = 'BRA'
BRN = 'BRN'
BGR = 'BGR'
BFA = 'BFA'
BDI = 'BDI'
KHM = 'KHM'
CMR = 'CMR'
CAN = 'CAN'
CPV = 'CPV'
CYM = 'CYM'
CAF = 'CAF'
TCD = 'TCD'
CHL = 'CHL'
CHN = 'CHN'
COD = 'COD'
COL = 'COL'
COM = 'COM'
COG = 'COG'
COK = 'COK'
CRI = 'CRI'
CIV = 'CIV'
HRV = 'HRV'
CUB = 'CUB'
CYP = 'CYP'
CZE = 'CZE'
DNK = 'DNK'
DJI = 'DJI'
DMA = 'DMA'
DOM = 'DOM'
ECU = 'ECU'
EGY = 'EGY'
SLV = 'SLV'
GNQ = 'GNQ'
ERI = 'ERI'
EST = 'EST'
ETH = 'ETH'
FLK = 'FLK'
FRO = 'FRO'
FJI = 'FJI'
FIN = 'FIN'
FRA = 'FRA'
GUF = 'GUF'
PYF = 'PYF'
GAB = 'GAB'
GMB = 'GMB'
GEO = 'GEO'
GGY = 'GGY'
DEU = 'DEU'
GHA = 'GHA'
GIB = 'GIB'
GRC = 'GRC'
GRL = 'GRL'
GRD = 'GRD'
GLP = 'GLP'
GUM = 'GUM'
GTM = 'GTM'
GIN = 'GIN'
GNB = 'GNB'
GUY = 'GUY'
HTI = 'HTI'
HND = 'HND'
HKG = 'HKG'
HUN = 'HUN'
ISL = 'ISL'
IND = 'IND'
IDN = 'IDN'
IMN = 'IMN'
IRN = 'IRN'
IRQ = 'IRQ'
IRL = 'IRL'
ISR = 'ISR'
ITA = 'ITA'
JAM = 'JAM'
JEY = 'JEY'
JPN = 'JPN'
JOR = 'JOR'
KAZ = 'KAZ'
KEN = 'KEN'
KIR = 'KIR'
PRK = 'PRK'
KOR = 'KOR'
KWT = 'KWT'
KGZ = 'KGZ'
LAO = 'LAO'
LVA = 'LVA'
LBN = 'LBN'
LSO = 'LSO'
LBR = 'LBR'
LBY = 'LBY'
LIE = 'LIE'
LTU = 'LTU'
LUX = 'LUX'
MAC = 'MAC'
MKD = 'MKD'
MDG = 'MDG'
MWI = 'MWI'
MYS = 'MYS'
MDV = 'MDV'
MLI = 'MLI'
MLT = 'MLT'
MHL = 'MHL'
MTQ = 'MTQ'
MRT = 'MRT'
MUS = 'MUS'
MYT = 'MYT'
MEX = 'MEX'
FSM = 'FSM'
MDA = 'MDA'
MCO = 'MCO'
MNE = 'MNE'
MNG = 'MNG'
MSR = 'MSR'
MAR = 'MAR'
MOZ = 'MOZ'
MMR = 'MMR'
NAM = 'NAM'
NRU = 'NRU'
NPL = 'NPL'
NLD = 'NLD'
ANT = 'ANT'
NCL = 'NCL'
NZL = 'NZL'
NIC = 'NIC'
NER = 'NER'
NGA = 'NGA'
NIU = 'NIU'
NFK = 'NFK'
MNP = 'MNP'
NOR = 'NOR'
OMN = 'OMN'
PAK = 'PAK'
PLW = 'PLW'
PAN = 'PAN'
PNG = 'PNG'
PRY = 'PRY'
PSE = 'PSE'
PER = 'PER'
PHL = 'PHL'
PCN = 'PCN'
POL = 'POL'
PRT = 'PRT'
PRI = 'PRI'
QAT = 'QAT'
REU = 'REU'
ROU = 'ROU'
RUS = 'RUS'
RWA = 'RWA'
KNA = 'KNA'
LCA = 'LCA'
VCT = 'VCT'
WSM = 'WSM'
SMR = 'SMR'
STP = 'STP'
SAU = 'SAU'
SEN = 'SEN'
SRB = 'SRB'
SYC = 'SYC'
SLE = 'SLE'
SGP = 'SGP'
SVK = 'SVK'
SVN = 'SVN'
SLB = 'SLB'
SOM = 'SOM'
ZAF = 'ZAF'
ESP = 'ESP'
LKA = 'LKA'
SHN = 'SHN'
SPM = 'SPM'
SDN = 'SDN'
SUR = 'SUR'
SJM = 'SJM'
SWZ = 'SWZ'
SWE = 'SWE'
CHE = 'CHE'
SYR = 'SYR'
TWN = 'TWN'
TJK = 'TJK'
TZA = 'TZA'
THA = 'THA'
TGO = 'TGO'
TKL = 'TKL'
TON = 'TON'
TTO = 'TTO'
TUN = 'TUN'
TUR = 'TUR'
TKM = 'TKM'
TLS = 'TLS'
TCA = 'TCA'
TUV = 'TUV'
UGA = 'UGA'
UKR = 'UKR'
ARE = 'ARE'
GBR = 'GBR'
USA = 'USA'
URY = 'URY'
UZB = 'UZB'
VUT = 'VUT'
VAT = 'VAT'
VEN = 'VEN'
VNM = 'VNM'
VGB = 'VGB'
VIR = 'VIR'
WLF = 'WLF'
ESH = 'ESH'
YEM = 'YEM'
ZAR = 'ZAR'
ZMB = 'ZMB'
ZWE = 'ZWE'
FISCAL = '01'
RECEPTOR = '02'
PAGADOR = '03'
COMPRADOR = '04'
COBRADOR = '05'
VENDEDOR = '06'
RECEPTOR_DEL_PAGO = '07'
RECEPTOR_DEL_COBRO = '08'
EMISOR = '09'
AFN = 'AFN'
ALL = 'ALL'
AMD = 'AMD'
ANG = 'ANG'
AOA = 'AOA'
ARS = 'ARS'
AUD = 'AUD'
AWG = 'AWG'
AZN = 'AZN'
BAD = 'BAD'
BBD = 'BBD'
BDT = 'BDT'
BGN = 'BGN'
BHD = 'BHD'
BIF = 'BIF'
BMD = 'BMD'
BND = 'BND'
BOB = 'BOB'
BRL = 'BRL'
BRR = 'BRR'
BSD = 'BSD'
BWP = 'BWP'
BYR = 'BYR'
BZD = 'BZD'
CAD = 'CAD'
CDF = 'CDF'
CDP = 'CDP'
CHF = 'CHF'
CLP = 'CLP'
CNY = 'CNY'
COP = 'COP'
CRC = 'CRC'
CUP = 'CUP'
CVE = 'CVE'
CZK = 'CZK'
DJF = 'DJF'
DKK = 'DKK'
DOP = 'DOP'
DRP = 'DRP'
DZD = 'DZD'
EEK = 'EEK'
EGP = 'EGP'
ETB = 'ETB'
EUR = 'EUR'
FJD = 'FJD'
FKP = 'FKP'
GBP = 'GBP'
GEK = 'GEK'
GHC = 'GHC'
GIP = 'GIP'
GMD = 'GMD'
GNF = 'GNF'
GTQ = 'GTQ'
GWP = 'GWP'
GYD = 'GYD'
HKD = 'HKD'
HNL = 'HNL'
HRK = 'HRK'
HTG = 'HTG'
HUF = 'HUF'
IDR = 'IDR'
ILS = 'ILS'
INR = 'INR'
IQD = 'IQD'
IRR = 'IRR'
ISK = 'ISK'
JMD = 'JMD'
JOD = 'JOD'
JPY = 'JPY'
KES = 'KES'
KGS = 'KGS'
KHR = 'KHR'
KMF = 'KMF'
KPW = 'KPW'
KRW = 'KRW'
KWD = 'KWD'
KYD = 'KYD'
KZT = 'KZT'
LAK = 'LAK'
LBP = 'LBP'
LKR = 'LKR'
LRD = 'LRD'
LSL = 'LSL'
LTL = 'LTL'
LVL = 'LVL'
LYD = 'LYD'
MAD = 'MAD'
MDL = 'MDL'
MGF = 'MGF'
MNC = 'MNC'
MNT = 'MNT'
MOP = 'MOP'
MRO = 'MRO'
MUR = 'MUR'
MVR = 'MVR'
MWK = 'MWK'
MXN = 'MXN'
MYR = 'MYR'
MZM = 'MZM'
NGN = 'NGN'
NIO = 'NIO'
NIS = 'NIS'
NOK = 'NOK'
NPR = 'NPR'
NZD = 'NZD'
OMR = 'OMR'
PAB = 'PAB'
PEI = 'PEI'
PEN = 'PEN'
PES = 'PES'
PGK = 'PGK'
PHP = 'PHP'
PKR = 'PKR'
PLN = 'PLN'
PYG = 'PYG'
QAR = 'QAR'
RMB = 'RMB'
RON = 'RON'
RUB = 'RUB'
RWF = 'RWF'
SAR = 'SAR'
SBD = 'SBD'
SCR = 'SCR'
SDP = 'SDP'
SEK = 'SEK'
SGD = 'SGD'
SHP = 'SHP'
SKK = 'SKK'
SLL = 'SLL'
SOL = 'SOL'
SOS = 'SOS'
SRD = 'SRD'
STD = 'STD'
SVC = 'SVC'
SYP = 'SYP'
SZL = 'SZL'
THB = 'THB'
TJS = 'TJS'
TMM = 'TMM'
TND = 'TND'
TOP = 'TOP'
TPE = 'TPE'
TRY = 'TRY'
TTD = 'TTD'
TWD = 'TWD'
TZS = 'TZS'
UAH = 'UAH'
UGS = 'UGS'
USD = 'USD'
UYP = 'UYP'
UYU = 'UYU'
VEF = 'VEF'
VND = 'VND'
VUV = 'VUV'
WST = 'WST'
XAF = 'XAF'
XCD = 'XCD'
XOF = 'XOF'
YER = 'YER'
ZMK = 'ZMK'
ZWD = 'ZWD'
ARABE = 'ar'
BIELORRUSO = 'be'
BULGARO = 'bg'
CATALAN = 'ca'
CHECO = 'cs'
DANES = 'da'
ALEMAN = 'de'
GRIEGO_MODERNO = 'el'
INGLES = 'en'
ESPANOL = 'es'
ESTONIO = 'et'
VASCUENCE = 'eu'
FINLANDES = 'fi'
FRANCES = 'fr'
GAELICO_DE_IRLANDA = 'ga'
GALLEGO = 'gl'
CROATA = 'hr'
HUNGARO = 'hu'
ISLANDES = 'is'
ITALIANO = 'it'
LETON = 'lv'
LITUANO = 'lt'
MACEDONIO = 'mk'
MALTES = 'mt'
NEERLANDES = 'nl'
NORUEGO = 'no'
POLACO = 'pl'
PORTUGUES = 'pt'
RUMANO = 'ro'
RUSO = 'ru'
ESLOVACO = 'sk'
ESLOVENO = 'sl'
ALBANES = 'sq'
SERBIO = 'sr'
SUECO = 'sv'
TURCO = 'tr'
UCRANIANO = 'uk'
NUMERO_DE_LA_FACTURA = '01'
SERIE_DE_LA_FACTURA = '02'
FECHA_EXPEDICION = '03'
NOMBRE_Y_APELLIDOS_RAZON_SOCIAL___EMISOR = '04'
NOMBRE_Y_APELLIDOS_RAZON_SOCIAL___RECEPTOR = '05'
IDENTIFICACION_FISCAL_EMISOR_OBLIGADO = '06'
IDENTIFICACION_FISCAL_RECEPTOR = '07'
DOMICILIO_EMISOR_OBLIGADO = '08'
DOMICILIO_RECEPTOR = '09'
DETALLE_OPERACION = '10'
PORCENTAJE_IMPOSITIVO_A_APLICAR = '11'
CUOTA_TRIBUTARIA_A_APLICAR = '12'
FECHA_PERIODO_A_APLICAR = '13'
CLASE_DE_FACTURA = '14'
LITERALES_LEGALES = '15'
BASE_IMPONIBLE = '16'
CALCULO_DE_CUOTAS_REPERCUTIDAS = '80'
CALCULO_DE_CUOTAS_RETENIDAS = '81'
BASE_IMPONIBLE_MODIFICADA_POR_DEVOLUCION_DE_ENVASES_EMBALAJES = '82'
BASE_IMPONIBLE_MODIFICADA_POR_DESCUENTOS_Y_BONIFICACIONES = '83'
BASE_IMPONIBLE_MODIFICADA_POR_RESOLUCION_FIRME_JUDICIAL_O_ADMINISTRATIVA = '84'
BASE_IMPONIBLE_MODIFICADA_CUOTAS_REPERCUTIDAS_NO_SATISFECHAS = '85'
NOMBRE_Y_APELLIDOS_RAZON_SOCIAL_EMISOR = 'Nombre y apellidos/Razón Social-Emisor'
NOMBRE_Y_APELLIDOS_RAZON_SOCIAL_RECEPTOR = 'Nombre y apellidos/Razón Social-Receptor'
BASE_IMPONIBLE_MODIFICADA_POR_DEVOLUCION_DE_ENVASES___EMBALAJES = 'Base imponible modificada por devolución de envases / embalajes'
RECTIFICACION_INTEGRA = '01'
RECTIFICACION_POR_DIFERENCIAS = '02'
RECTIFICACION_POR_DESCUENTO_POR_VOLUMEN_DE_OPERACIONES_DURANTE_UN_PERIODO = '03'
AUTORIZADAS_POR_LA_AGENCIA_TRIBUTARIA = '04'
AL_CONTADO = '01'
RECIBO_DOMICILIADO = '02'
RECIBO = '03'
TRANSFERENCIA = '04'
LETRA_ACEPTADA = '05'
CREDITO_DOCUMENTARIO = '06'
CONTRATO_ADJUDICACION = '07'
LETRA_DE_CAMBIO = '08'
PAGARE_A_LA__ORDEN = '09'
PAGARE_NO_A_LA_ORDEN = '10'
CHEQUE = '11'
REPOSICION = '12'
ESPECIALES = '13'
COMPENSACION = '14'
GIRO_POSTAL = '15'
CHEQUE_CONFORMADO = '16'
CHEQUE_BANCARIO = '17'
PAGO_CONTRA_REEMBOLSO = '18'
PAGO_MEDIANTE_TARJETA = '19'
IVA = '01'
IPSI = '02'
IGIC = '03'
IRPF = '04'
OTRO = '05'
ITPAJD = '06'
IE = '07'
RA = '08'
IGTECM = '09'
IECDPCAC = '10'
IIIMAB = '11'
ICIO = '12'
IMVDN = '13'
IMSN = '14'
IMGSN = '15'
IMPN = '16'
REIVA = '17'
REIGIC = '18'
REIPSI = '19'
IPS = '20'
RLEA = '21'
IVPEE = '22'
IMPUESTO_SOBRE_LA_PRODUCCION_DE_COMBUSTIBLE_NUCLEAR_GASTADO_Y_RESIDUOS_RADIACTIVOS_RESULTANTES_DE_LA_GENERACION_DE_ENERGIA_NUCLEOELECTRICA = '23'
IMPUESTO_SOBRE_EL_ALMACENAMIENTO_DE_COMBUSTIBLE_NUCLEAR_GASTADO_Y_RESIDUOS_RADIOACTIVOS_EN_INSTALACIONES_CENTRALIZADAS = '24'
IDEC = '25'
IMPUESTO_SOBRE_LAS_LABORES_DEL_TABACO_EN_LA_COMUNIDAD_AUTONOMA_DE_CANARIAS = '26'
IGFEI = '27'
IRNR = '28'
IMPUESTO_SOBRE_SOCIEDADES = '29'
FACTURA_COMPLETA = 'FC'
FACTURA_ABREVIADA = 'FA'
AUTOFACTURA = 'AF'
ORIGINAL = 'OO'
ORIGINAL_RECTIFICATIVA = 'OR'
ORIGINAL_RECAPITULATIVA = 'OC'
COPIA_ORIGINAL = 'CO'
COPIA_RECTIFICATIVA = 'CR'
COPIA_RECAPITULATIVA = 'CC'
UNIDADES = '01'
HORAS_HUR = '02'
KILOGRAMOS_KGM = '03'
LITROS_LTR = '04'
OTROS = '05'
CAJAS_BX = '06'
BANDEJAS_DS = '07'
BARRILES_BA = '08'
BIDONES_JY = '09'
BOLSAS_BG = '10'
BOMBONAS_CO = '11'
BOTELLAS_BO = '12'
BOTES_CI = '13'
TETRA_BRIKS = '14'
CENTILITROS_CLT = '15'
CENTIMETROS_CMT = '16'
CUBOS_BI = '17'
DOCENAS = '18'
ESTUCHES_CS = '19'
GARRAFAS_DJ = '20'
GRAMOS_GRM = '21'
KILOMETROS_KMT = '22'
LATAS_CA = '23'
MANOJOS_BH = '24'
METROS_MTR = '25'
MILIMETROS_MMT = '26'
_PACKS = '27'
PAQUETES_PK = '28'
RACIONES = '29'
ROLLOS_RO = '30'
SOBRES_EN = '31'
TARRINAS_TB = '32'
METRO_CUBICO_MTQ = '33'
SEGUNDO_SEC = '34'
VATIO_WTT = '35'
INDIVIDUAL = 'I'
LOTE = 'L'
PROVEEDOR = 'EM'
CLIENTE = 'RE'
TERCERO = 'TE'
SpecialTaxableEventCodeType = (
	(OPERACION_SUJETA_Y_EXENTA, 'Operación sujeta y exenta'),
	(OPERACION_NO_SUJETA, 'Operación no sujeta')
)

AttachmentCompressionAlgorithmType = (
	(ZIP, 'ZIP'),
	(GZIP, 'GZIP'),
	(NONE, 'NONE')
)

AttachmentFormatType = (
	(XML, 'xml'),
	(DOC, 'doc'),
	(GIF, 'gif'),
	(RTF, 'rtf'),
	(PDF, 'pdf'),
	(XLS, 'xls'),
	(JPG, 'jpg'),
	(BMP, 'bmp'),
	(TIFF, 'tiff')
)

AttachmentEncodingType = (
	(BASE, 'BASE64'),
	(BER, 'BER'),
	(DER, 'DER'),
	(NONE, 'NONE')
)

PersonTypeCodeType = (
	(PERSONA_FISICA, 'Persona física.'),
	(PERSONA_JURIDICA, 'Persona jurídica.')
)

ResidenceTypeCodeType = (
	(EXTRANJERO, 'Extranjero (Fuera Unión Europea).'),
	(RESIDENTE, 'Residente (en España).'),
	(RESIDENTE_EN_LA_UNION_EUROPEA, 'Residente en la Unión Europea (excepto España).')
)

CountryType = (
	(AFG, 'AFG'),
	(ALB, 'ALB'),
	(DZA, 'DZA'),
	(ASM, 'ASM'),
	(AND, 'AND'),
	(AGO, 'AGO'),
	(AIA, 'AIA'),
	(ATG, 'ATG'),
	(ARG, 'ARG'),
	(ARM, 'ARM'),
	(ABW, 'ABW'),
	(AUS, 'AUS'),
	(AUT, 'AUT'),
	(AZE, 'AZE'),
	(BHS, 'BHS'),
	(BHR, 'BHR'),
	(BGD, 'BGD'),
	(BRB, 'BRB'),
	(BLR, 'BLR'),
	(BEL, 'BEL'),
	(BLZ, 'BLZ'),
	(BEN, 'BEN'),
	(BMU, 'BMU'),
	(BTN, 'BTN'),
	(BOL, 'BOL'),
	(BIH, 'BIH'),
	(BWA, 'BWA'),
	(BRA, 'BRA'),
	(BRN, 'BRN'),
	(BGR, 'BGR'),
	(BFA, 'BFA'),
	(BDI, 'BDI'),
	(KHM, 'KHM'),
	(CMR, 'CMR'),
	(CAN, 'CAN'),
	(CPV, 'CPV'),
	(CYM, 'CYM'),
	(CAF, 'CAF'),
	(TCD, 'TCD'),
	(CHL, 'CHL'),
	(CHN, 'CHN'),
	(COD, 'COD'),
	(COL, 'COL'),
	(COM, 'COM'),
	(COG, 'COG'),
	(COK, 'COK'),
	(CRI, 'CRI'),
	(CIV, 'CIV'),
	(HRV, 'HRV'),
	(CUB, 'CUB'),
	(CYP, 'CYP'),
	(CZE, 'CZE'),
	(DNK, 'DNK'),
	(DJI, 'DJI'),
	(DMA, 'DMA'),
	(DOM, 'DOM'),
	(ECU, 'ECU'),
	(EGY, 'EGY'),
	(SLV, 'SLV'),
	(GNQ, 'GNQ'),
	(ERI, 'ERI'),
	(EST, 'EST'),
	(ETH, 'ETH'),
	(FLK, 'FLK'),
	(FRO, 'FRO'),
	(FJI, 'FJI'),
	(FIN, 'FIN'),
	(FRA, 'FRA'),
	(GUF, 'GUF'),
	(PYF, 'PYF'),
	(GAB, 'GAB'),
	(GMB, 'GMB'),
	(GEO, 'GEO'),
	(GGY, 'GGY'),
	(DEU, 'DEU'),
	(GHA, 'GHA'),
	(GIB, 'GIB'),
	(GRC, 'GRC'),
	(GRL, 'GRL'),
	(GRD, 'GRD'),
	(GLP, 'GLP'),
	(GUM, 'GUM'),
	(GTM, 'GTM'),
	(GIN, 'GIN'),
	(GNB, 'GNB'),
	(GUY, 'GUY'),
	(HTI, 'HTI'),
	(HND, 'HND'),
	(HKG, 'HKG'),
	(HUN, 'HUN'),
	(ISL, 'ISL'),
	(IND, 'IND'),
	(IDN, 'IDN'),
	(IMN, 'IMN'),
	(IRN, 'IRN'),
	(IRQ, 'IRQ'),
	(IRL, 'IRL'),
	(ISR, 'ISR'),
	(ITA, 'ITA'),
	(JAM, 'JAM'),
	(JEY, 'JEY'),
	(JPN, 'JPN'),
	(JOR, 'JOR'),
	(KAZ, 'KAZ'),
	(KEN, 'KEN'),
	(KIR, 'KIR'),
	(PRK, 'PRK'),
	(KOR, 'KOR'),
	(KWT, 'KWT'),
	(KGZ, 'KGZ'),
	(LAO, 'LAO'),
	(LVA, 'LVA'),
	(LBN, 'LBN'),
	(LSO, 'LSO'),
	(LBR, 'LBR'),
	(LBY, 'LBY'),
	(LIE, 'LIE'),
	(LTU, 'LTU'),
	(LUX, 'LUX'),
	(MAC, 'MAC'),
	(MKD, 'MKD'),
	(MDG, 'MDG'),
	(MWI, 'MWI'),
	(MYS, 'MYS'),
	(MDV, 'MDV'),
	(MLI, 'MLI'),
	(MLT, 'MLT'),
	(MHL, 'MHL'),
	(MTQ, 'MTQ'),
	(MRT, 'MRT'),
	(MUS, 'MUS'),
	(MYT, 'MYT'),
	(MEX, 'MEX'),
	(FSM, 'FSM'),
	(MDA, 'MDA'),
	(MCO, 'MCO'),
	(MNE, 'MNE'),
	(MNG, 'MNG'),
	(MSR, 'MSR'),
	(MAR, 'MAR'),
	(MOZ, 'MOZ'),
	(MMR, 'MMR'),
	(NAM, 'NAM'),
	(NRU, 'NRU'),
	(NPL, 'NPL'),
	(NLD, 'NLD'),
	(ANT, 'ANT'),
	(NCL, 'NCL'),
	(NZL, 'NZL'),
	(NIC, 'NIC'),
	(NER, 'NER'),
	(NGA, 'NGA'),
	(NIU, 'NIU'),
	(NFK, 'NFK'),
	(MNP, 'MNP'),
	(NOR, 'NOR'),
	(OMN, 'OMN'),
	(PAK, 'PAK'),
	(PLW, 'PLW'),
	(PAN, 'PAN'),
	(PNG, 'PNG'),
	(PRY, 'PRY'),
	(PSE, 'PSE'),
	(PER, 'PER'),
	(PHL, 'PHL'),
	(PCN, 'PCN'),
	(POL, 'POL'),
	(PRT, 'PRT'),
	(PRI, 'PRI'),
	(QAT, 'QAT'),
	(REU, 'REU'),
	(ROU, 'ROU'),
	(RUS, 'RUS'),
	(RWA, 'RWA'),
	(KNA, 'KNA'),
	(LCA, 'LCA'),
	(VCT, 'VCT'),
	(WSM, 'WSM'),
	(SMR, 'SMR'),
	(STP, 'STP'),
	(SAU, 'SAU'),
	(SEN, 'SEN'),
	(SRB, 'SRB'),
	(SYC, 'SYC'),
	(SLE, 'SLE'),
	(SGP, 'SGP'),
	(SVK, 'SVK'),
	(SVN, 'SVN'),
	(SLB, 'SLB'),
	(SOM, 'SOM'),
	(ZAF, 'ZAF'),
	(ESP, 'ESP'),
	(LKA, 'LKA'),
	(SHN, 'SHN'),
	(SPM, 'SPM'),
	(SDN, 'SDN'),
	(SUR, 'SUR'),
	(SJM, 'SJM'),
	(SWZ, 'SWZ'),
	(SWE, 'SWE'),
	(CHE, 'CHE'),
	(SYR, 'SYR'),
	(TWN, 'TWN'),
	(TJK, 'TJK'),
	(TZA, 'TZA'),
	(THA, 'THA'),
	(TGO, 'TGO'),
	(TKL, 'TKL'),
	(TON, 'TON'),
	(TTO, 'TTO'),
	(TUN, 'TUN'),
	(TUR, 'TUR'),
	(TKM, 'TKM'),
	(TLS, 'TLS'),
	(TCA, 'TCA'),
	(TUV, 'TUV'),
	(UGA, 'UGA'),
	(UKR, 'UKR'),
	(ARE, 'ARE'),
	(GBR, 'GBR'),
	(USA, 'USA'),
	(URY, 'URY'),
	(UZB, 'UZB'),
	(VUT, 'VUT'),
	(VAT, 'VAT'),
	(VEN, 'VEN'),
	(VNM, 'VNM'),
	(VGB, 'VGB'),
	(VIR, 'VIR'),
	(WLF, 'WLF'),
	(ESH, 'ESH'),
	(YEM, 'YEM'),
	(ZAR, 'ZAR'),
	(ZMB, 'ZMB'),
	(ZWE, 'ZWE')
)

RoleTypeCodeType = (
	(FISCAL, 'Fiscal'),
	(RECEPTOR, 'Receptor'),
	(PAGADOR, 'Pagador'),
	(COMPRADOR, 'Comprador'),
	(COBRADOR, 'Cobrador'),
	(VENDEDOR, 'Vendedor'),
	(RECEPTOR_DEL_PAGO, 'Receptor del pago'),
	(RECEPTOR_DEL_COBRO, 'Receptor del cobro'),
	(EMISOR, 'Emisor')
)

CurrencyCodeType = (
	(AFN, 'AFN'),
	(ALL, 'ALL'),
	(AMD, 'AMD'),
	(ANG, 'ANG'),
	(AOA, 'AOA'),
	(ARS, 'ARS'),
	(AUD, 'AUD'),
	(AWG, 'AWG'),
	(AZN, 'AZN'),
	(BAD, 'BAD'),
	(BBD, 'BBD'),
	(BDT, 'BDT'),
	(BGN, 'BGN'),
	(BHD, 'BHD'),
	(BIF, 'BIF'),
	(BMD, 'BMD'),
	(BND, 'BND'),
	(BOB, 'BOB'),
	(BRL, 'BRL'),
	(BRR, 'BRR'),
	(BSD, 'BSD'),
	(BWP, 'BWP'),
	(BYR, 'BYR'),
	(BZD, 'BZD'),
	(CAD, 'CAD'),
	(CDF, 'CDF'),
	(CDP, 'CDP'),
	(CHF, 'CHF'),
	(CLP, 'CLP'),
	(CNY, 'CNY'),
	(COP, 'COP'),
	(CRC, 'CRC'),
	(CUP, 'CUP'),
	(CVE, 'CVE'),
	(CZK, 'CZK'),
	(DJF, 'DJF'),
	(DKK, 'DKK'),
	(DOP, 'DOP'),
	(DRP, 'DRP'),
	(DZD, 'DZD'),
	(EEK, 'EEK'),
	(EGP, 'EGP'),
	(ESP, 'ESP'),
	(ETB, 'ETB'),
	(EUR, 'EUR'),
	(FJD, 'FJD'),
	(FKP, 'FKP'),
	(GBP, 'GBP'),
	(GEK, 'GEK'),
	(GHC, 'GHC'),
	(GIP, 'GIP'),
	(GMD, 'GMD'),
	(GNF, 'GNF'),
	(GTQ, 'GTQ'),
	(GWP, 'GWP'),
	(GYD, 'GYD'),
	(HKD, 'HKD'),
	(HNL, 'HNL'),
	(HRK, 'HRK'),
	(HTG, 'HTG'),
	(HUF, 'HUF'),
	(IDR, 'IDR'),
	(ILS, 'ILS'),
	(INR, 'INR'),
	(IQD, 'IQD'),
	(IRR, 'IRR'),
	(ISK, 'ISK'),
	(JMD, 'JMD'),
	(JOD, 'JOD'),
	(JPY, 'JPY'),
	(KES, 'KES'),
	(KGS, 'KGS'),
	(KHR, 'KHR'),
	(KMF, 'KMF'),
	(KPW, 'KPW'),
	(KRW, 'KRW'),
	(KWD, 'KWD'),
	(KYD, 'KYD'),
	(KZT, 'KZT'),
	(LAK, 'LAK'),
	(LBP, 'LBP'),
	(LKR, 'LKR'),
	(LRD, 'LRD'),
	(LSL, 'LSL'),
	(LTL, 'LTL'),
	(LVL, 'LVL'),
	(LYD, 'LYD'),
	(MAD, 'MAD'),
	(MDL, 'MDL'),
	(MGF, 'MGF'),
	(MNC, 'MNC'),
	(MNT, 'MNT'),
	(MOP, 'MOP'),
	(MRO, 'MRO'),
	(MUR, 'MUR'),
	(MVR, 'MVR'),
	(MWK, 'MWK'),
	(MXN, 'MXN'),
	(MYR, 'MYR'),
	(MZM, 'MZM'),
	(NGN, 'NGN'),
	(NIC, 'NIC'),
	(NIO, 'NIO'),
	(NIS, 'NIS'),
	(NOK, 'NOK'),
	(NPR, 'NPR'),
	(NZD, 'NZD'),
	(OMR, 'OMR'),
	(PAB, 'PAB'),
	(PEI, 'PEI'),
	(PEN, 'PEN'),
	(PES, 'PES'),
	(PGK, 'PGK'),
	(PHP, 'PHP'),
	(PKR, 'PKR'),
	(PLN, 'PLN'),
	(PYG, 'PYG'),
	(QAR, 'QAR'),
	(RMB, 'RMB'),
	(RON, 'RON'),
	(RUB, 'RUB'),
	(RWF, 'RWF'),
	(SAR, 'SAR'),
	(SBD, 'SBD'),
	(SCR, 'SCR'),
	(SDP, 'SDP'),
	(SEK, 'SEK'),
	(SGD, 'SGD'),
	(SHP, 'SHP'),
	(SKK, 'SKK'),
	(SLL, 'SLL'),
	(SOL, 'SOL'),
	(SOS, 'SOS'),
	(SRD, 'SRD'),
	(STD, 'STD'),
	(SVC, 'SVC'),
	(SYP, 'SYP'),
	(SZL, 'SZL'),
	(THB, 'THB'),
	(TJS, 'TJS'),
	(TMM, 'TMM'),
	(TND, 'TND'),
	(TOP, 'TOP'),
	(TPE, 'TPE'),
	(TRY, 'TRY'),
	(TTD, 'TTD'),
	(TWD, 'TWD'),
	(TZS, 'TZS'),
	(UAH, 'UAH'),
	(UGS, 'UGS'),
	(USD, 'USD'),
	(UYP, 'UYP'),
	(UYU, 'UYU'),
	(VEF, 'VEF'),
	(VND, 'VND'),
	(VUV, 'VUV'),
	(WST, 'WST'),
	(XAF, 'XAF'),
	(XCD, 'XCD'),
	(XOF, 'XOF'),
	(YER, 'YER'),
	(ZAR, 'ZAR'),
	(ZMK, 'ZMK'),
	(ZWD, 'ZWD')
)

LanguageCodeType = (
	(ARABE, 'Arabe'),
	(BIELORRUSO, 'Bielorruso'),
	(BULGARO, 'Búlgaro'),
	(CATALAN, 'Catalán'),
	(CHECO, 'Checo'),
	(DANES, 'Danés'),
	(ALEMAN, 'Alemán'),
	(GRIEGO_MODERNO, 'Griego moderno'),
	(INGLES, 'Inglés'),
	(ESPANOL, 'Español'),
	(ESTONIO, 'Estonio'),
	(VASCUENCE, 'Vascuence'),
	(FINLANDES, 'Finlandés'),
	(FRANCES, 'Francés'),
	(GAELICO_DE_IRLANDA, 'Gaélico de Irlanda'),
	(GALLEGO, 'Gallego'),
	(CROATA, 'Croata'),
	(HUNGARO, 'Húngaro'),
	(ISLANDES, 'Islandés'),
	(ITALIANO, 'Italiano'),
	(LETON, 'Letón'),
	(LITUANO, 'Lituano'),
	(MACEDONIO, 'Macedonio'),
	(MALTES, 'Maltés'),
	(NEERLANDES, 'Neerlandés'),
	(NORUEGO, 'Noruego'),
	(POLACO, 'Polaco'),
	(PORTUGUES, 'Portugués'),
	(RUMANO, 'Rumano'),
	(RUSO, 'Ruso'),
	(ESLOVACO, 'Eslovaco'),
	(ESLOVENO, 'Esloveno'),
	(ALBANES, 'Albanés'),
	(SERBIO, 'Serbio'),
	(SUECO, 'Sueco'),
	(TURCO, 'Turco'),
	(UCRANIANO, 'Ucraniano')
)

ReasonCodeType = (
	(NUMERO_DE_LA_FACTURA, '"Número de la factura"'),
	(SERIE_DE_LA_FACTURA, '"Serie de la factura"'),
	(FECHA_EXPEDICION, '"Fecha expedición"'),
	(NOMBRE_Y_APELLIDOS_RAZON_SOCIAL___EMISOR, '"Nombre y apellidos/Razón social - Emisor"'),
	(NOMBRE_Y_APELLIDOS_RAZON_SOCIAL___RECEPTOR, '"Nombre y apellidos/Razón social - Receptor"'),
	(IDENTIFICACION_FISCAL_EMISOR_OBLIGADO, '"Identificación fiscal Emisor/Obligado"'),
	(IDENTIFICACION_FISCAL_RECEPTOR, '"Identificación fiscal Receptor"'),
	(DOMICILIO_EMISOR_OBLIGADO, '"Domicilio Emisor/Obligado"'),
	(DOMICILIO_RECEPTOR, '"Domicilio Receptor"'),
	(DETALLE_OPERACION, '"Detalle Operación"'),
	(PORCENTAJE_IMPOSITIVO_A_APLICAR, '"Porcentaje impositivo a aplicar"'),
	(CUOTA_TRIBUTARIA_A_APLICAR, '"Cuota tributaria a aplicar"'),
	(FECHA_PERIODO_A_APLICAR, '"Fecha/Periodo a aplicar"'),
	(CLASE_DE_FACTURA, '"Clase de factura"'),
	(LITERALES_LEGALES, '"Literales legales"'),
	(BASE_IMPONIBLE, '"Base imponible"'),
	(CALCULO_DE_CUOTAS_REPERCUTIDAS, '"Cálculo de cuotas repercutidas"'),
	(CALCULO_DE_CUOTAS_RETENIDAS, '"Cálculo de cuotas retenidas"'),
	(BASE_IMPONIBLE_MODIFICADA_POR_DEVOLUCION_DE_ENVASES_EMBALAJES, '"Base imponible modificada por devolución de envases/embalajes"'),
	(BASE_IMPONIBLE_MODIFICADA_POR_DESCUENTOS_Y_BONIFICACIONES, '"Base imponible modificada por descuentos y bonificaciones"'),
	(BASE_IMPONIBLE_MODIFICADA_POR_RESOLUCION_FIRME_JUDICIAL_O_ADMINISTRATIVA, '"Base imponible modificada por resolución firme, judicial o administrativa"'),
	(BASE_IMPONIBLE_MODIFICADA_CUOTAS_REPERCUTIDAS_NO_SATISFECHAS, '"Base imponible modificada cuotas repercutidas no satisfechas. Auto de declaración de concurso"')
)

ReasonDescriptionType = (
	(NUMERO_DE_LA_FACTURA, 'Número de la factura'),
	(SERIE_DE_LA_FACTURA, 'Serie de la factura'),
	(FECHA_EXPEDICION, 'Fecha expedición'),
	(NOMBRE_Y_APELLIDOS_RAZON_SOCIAL_EMISOR, 'Nombre y apellidos/Razón Social-Emisor'),
	(NOMBRE_Y_APELLIDOS_RAZON_SOCIAL_RECEPTOR, 'Nombre y apellidos/Razón Social-Receptor'),
	(IDENTIFICACION_FISCAL_EMISOR_OBLIGADO, 'Identificación fiscal Emisor/obligado'),
	(IDENTIFICACION_FISCAL_RECEPTOR, 'Identificación fiscal Receptor'),
	(DOMICILIO_EMISOR_OBLIGADO, 'Domicilio Emisor/Obligado'),
	(DOMICILIO_RECEPTOR, 'Domicilio Receptor'),
	(DETALLE_OPERACION, 'Detalle Operación'),
	(PORCENTAJE_IMPOSITIVO_A_APLICAR, 'Porcentaje impositivo a aplicar'),
	(CUOTA_TRIBUTARIA_A_APLICAR, 'Cuota tributaria a aplicar'),
	(FECHA_PERIODO_A_APLICAR, 'Fecha/Periodo a aplicar'),
	(CLASE_DE_FACTURA, 'Clase de factura'),
	(LITERALES_LEGALES, 'Literales legales'),
	(BASE_IMPONIBLE, 'Base imponible'),
	(CALCULO_DE_CUOTAS_REPERCUTIDAS, 'Cálculo de cuotas repercutidas'),
	(CALCULO_DE_CUOTAS_RETENIDAS, 'Cálculo de cuotas retenidas'),
	(BASE_IMPONIBLE_MODIFICADA_POR_DEVOLUCION_DE_ENVASES___EMBALAJES, 'Base imponible modificada por devolución de envases / embalajes'),
	(BASE_IMPONIBLE_MODIFICADA_POR_DESCUENTOS_Y_BONIFICACIONES, 'Base imponible modificada por descuentos y bonificaciones'),
	(BASE_IMPONIBLE_MODIFICADA_POR_RESOLUCION_FIRME_JUDICIAL_O_ADMINISTRATIVA, 'Base imponible modificada por resolución firme, judicial o administrativa'),
	(BASE_IMPONIBLE_MODIFICADA_CUOTAS_REPERCUTIDAS_NO_SATISFECHAS, 'Base imponible modificada cuotas repercutidas no satisfechas. Auto de declaración de concurso')
)

CorrectionMethodType = (
	(RECTIFICACION_INTEGRA, '"Rectificación íntegra"'),
	(RECTIFICACION_POR_DIFERENCIAS, '"Rectificación por diferencias"'),
	(RECTIFICACION_POR_DESCUENTO_POR_VOLUMEN_DE_OPERACIONES_DURANTE_UN_PERIODO, '"Rectificación por descuento por volumen de operaciones durante un periodo"'),
	(AUTORIZADAS_POR_LA_AGENCIA_TRIBUTARIA, '"Autorizadas por la Agencia Tributaria"')
)

CorrectionMethodDescriptionType = (
	(RECTIFICACION_INTEGRA, 'Rectificación íntegra'),
	(RECTIFICACION_POR_DIFERENCIAS, 'Rectificación por diferencias'),
	(RECTIFICACION_POR_DESCUENTO_POR_VOLUMEN_DE_OPERACIONES_DURANTE_UN_PERIODO, 'Rectificación por descuento por volumen de operaciones durante un periodo'),
	(AUTORIZADAS_POR_LA_AGENCIA_TRIBUTARIA, 'Autorizadas por la Agencia Tributaria')
)

PaymentMeansType = (
	(AL_CONTADO, 'Al contado'),
	(RECIBO_DOMICILIADO, 'Recibo Domiciliado'),
	(RECIBO, 'Recibo'),
	(TRANSFERENCIA, 'Transferencia'),
	(LETRA_ACEPTADA, 'Letra Aceptada'),
	(CREDITO_DOCUMENTARIO, 'Crédito Documentario'),
	(CONTRATO_ADJUDICACION, 'Contrato Adjudicación'),
	(LETRA_DE_CAMBIO, 'Letra de cambio'),
	(PAGARE_A_LA__ORDEN, 'Pagaré a la  Orden'),
	(PAGARE_NO_A_LA_ORDEN, 'Pagaré No a la Orden'),
	(CHEQUE, 'Cheque'),
	(REPOSICION, 'Reposición'),
	(ESPECIALES, 'Especiales'),
	(COMPENSACION, 'Compensación'),
	(GIRO_POSTAL, 'Giro postal'),
	(CHEQUE_CONFORMADO, 'Cheque conformado'),
	(CHEQUE_BANCARIO, 'Cheque bancario'),
	(PAGO_CONTRA_REEMBOLSO, 'Pago contra reembolso'),
	(PAGO_MEDIANTE_TARJETA, 'Pago mediante tarjeta')
)

TaxTypeCodeType = (
	(IVA, 'IVA: Impuesto sobre el valor añadido'),
	(IPSI, 'IPSI: Impuesto sobre la producción, los servicios y la importación'),
	(IGIC, 'IGIC: Impuesto general indirecto de Canarias'),
	(IRPF, 'IRPF: Impuesto sobre la Renta de las personas físicas'),
	(OTRO, 'Otro'),
	(ITPAJD, 'ITPAJD: Impuesto sobre transmisiones patrimoniales y actos jurídicos documentados'),
	(IE, 'IE: Impuestos especiales'),
	(RA, 'Ra: Renta aduanas'),
	(IGTECM, 'IGTECM: Impuesto general sobre el tráfico de empresas que se aplica en Ceuta y Melilla'),
	(IECDPCAC, 'IECDPCAC: Impuesto especial sobre los combustibles derivados del petróleo en la Comunidad Autonoma Canaria'),
	(IIIMAB, 'IIIMAB: Impuesto sobre las instalaciones que inciden sobre el medio ambiente en las Baleares'),
	(ICIO, 'ICIO: Impuesto sobre las construcciones, instalaciones y obras'),
	(IMVDN, 'IMVDN: Impuesto municipal sobre las viviendas desocupadas en Navarra'),
	(IMSN, 'IMSN: Impuesto municipal sobre solares en Navarra'),
	(IMGSN, 'IMGSN: Impuesto municipal sobre gastos suntuarios en Navarra'),
	(IMPN, 'IMPN: Impuesto municipal sobre publicidad en Navarra'),
	(REIVA, 'REIVA: Régimen especial de IVA para agencias de viajes'),
	(REIGIC, 'REIGIC: Régimen especial de IGIC: para agencias de viajes'),
	(REIPSI, 'REIPSI: Régimen especial de IPSI para agencias de viajes'),
	(IPS, 'IPS: Impuestos sobre las primas de seguros'),
	(RLEA, 'RLEA: Recargo destinado a financiar las funciones de liquidación de entidades aseguradoras'),
	(IVPEE, 'IVPEE: Impuesto sobre el valor de la producción de la energía eléctrica'),
	(IMPUESTO_SOBRE_LA_PRODUCCION_DE_COMBUSTIBLE_NUCLEAR_GASTADO_Y_RESIDUOS_RADIACTIVOS_RESULTANTES_DE_LA_GENERACION_DE_ENERGIA_NUCLEOELECTRICA, 'Impuesto sobre la producción de combustible nuclear gastado y residuos radiactivos resultantes de la generación de energía nucleoeléctrica'),
	(IMPUESTO_SOBRE_EL_ALMACENAMIENTO_DE_COMBUSTIBLE_NUCLEAR_GASTADO_Y_RESIDUOS_RADIOACTIVOS_EN_INSTALACIONES_CENTRALIZADAS, 'Impuesto sobre el almacenamiento de combustible nuclear gastado y residuos radioactivos en instalaciones centralizadas'),
	(IDEC, 'IDEC: Impuesto sobre los Depósitos en las Entidades de Crédito'),
	(IMPUESTO_SOBRE_LAS_LABORES_DEL_TABACO_EN_LA_COMUNIDAD_AUTONOMA_DE_CANARIAS, 'Impuesto sobre las labores del tabaco en la Comunidad Autónoma de Canarias'),
	(IGFEI, 'IGFEI: Impuesto sobre los Gases Fluorados de Efecto Invernadero'),
	(IRNR, 'IRNR: Impuesto sobre la Renta de No Residentes'),
	(IMPUESTO_SOBRE_SOCIEDADES, 'Impuesto sobre Sociedades')
)

InvoiceDocumentTypeType = (
	(FACTURA_COMPLETA, 'Factura Completa.'),
	(FACTURA_ABREVIADA, 'Factura abreviada.'),
	(AUTOFACTURA, 'AutoFactura.')
)

InvoiceClassType = (
	(ORIGINAL, 'Original.'),
	(ORIGINAL_RECTIFICATIVA, 'Original rectificativa'),
	(ORIGINAL_RECAPITULATIVA, 'Original recapitulativa.'),
	(COPIA_ORIGINAL, 'Copia original.'),
	(COPIA_RECTIFICATIVA, 'Copia rectificativa.'),
	(COPIA_RECAPITULATIVA, 'Copia recapitulativa.')
)

UnitOfMeasureType = (
	(UNIDADES, 'Unidades'),
	(HORAS_HUR, 'Horas-HUR'),
	(KILOGRAMOS_KGM, 'Kilogramos-KGM'),
	(LITROS_LTR, 'Litros-LTR'),
	(OTROS, 'Otros'),
	(CAJAS_BX, 'Cajas-BX'),
	(BANDEJAS_DS, 'Bandejas-DS'),
	(BARRILES_BA, 'Barriles-BA'),
	(BIDONES_JY, 'Bidones-JY'),
	(BOLSAS_BG, 'Bolsas-BG'),
	(BOMBONAS_CO, 'Bombonas-CO'),
	(BOTELLAS_BO, 'Botellas-BO'),
	(BOTES_CI, 'Botes-CI'),
	(TETRA_BRIKS, 'Tetra Briks'),
	(CENTILITROS_CLT, 'Centilitros-CLT'),
	(CENTIMETROS_CMT, 'Centímetros-CMT'),
	(CUBOS_BI, 'Cubos-BI'),
	(DOCENAS, 'Docenas'),
	(ESTUCHES_CS, 'Estuches-CS'),
	(GARRAFAS_DJ, 'Garrafas-DJ'),
	(GRAMOS_GRM, 'Gramos-GRM'),
	(KILOMETROS_KMT, 'Kilómetros-KMT'),
	(LATAS_CA, 'Latas-CA'),
	(MANOJOS_BH, 'Manojos-BH'),
	(METROS_MTR, 'Metros-MTR'),
	(MILIMETROS_MMT, 'Milímetros-MMT'),
	(_PACKS, '6-Packs'),
	(PAQUETES_PK, 'Paquetes-PK'),
	(RACIONES, 'Raciones'),
	(ROLLOS_RO, 'Rollos-RO'),
	(SOBRES_EN, 'Sobres-EN'),
	(TARRINAS_TB, 'Tarrinas-TB'),
	(METRO_CUBICO_MTQ, 'Metro cúbico-MTQ'),
	(SEGUNDO_SEC, 'Segundo-SEC'),
	(VATIO_WTT, 'Vatio-WTT')
)

ModalityType = (
	(INDIVIDUAL, 'Individual'),
	(LOTE, 'Lote')
)

InvoiceIssuerTypeType = (
	(PROVEEDOR, 'Proveedor (Emisor).'),
	(CLIENTE, 'Cliente (Receptor).'),
	(TERCERO, 'Tercero.')
)

class ExchangeRateDetailsType(models.Model):
	ExchangeRate = models.DecimalField(null=True,max_digits=19,decimal_places=10,blank=True) #  Tipo de Cambio. Artº 79.once de la Ley 37/92 de 28 de diciembre del Impuesto sobre el Valor Añadido. Cambio vendedor fijado por el Banco de España y vigente en el momento del devengo. Hasta ocho decimales.
	ExchangeRateDate = models.DateTimeField(null=True,blank=True) #  Fecha de publicación del tipo de cambio aplicado. ISO 8601:2004.

class PlaceOfIssueType(models.Model):
	PostCode = models.CharField(max_length=5,null=True,blank=True) #  Código postal. Asignado por Correos.
	PlaceOfIssueDescription = models.CharField(max_length=20,null=True,blank=True) #  Texto del nombre del lugar.

class DeliveryNoteType(models.Model):
	DeliveryNoteNumber = models.CharField(max_length=30,null=True,blank=True) #  Número de referencia del albarán.
	DeliveryNoteDate = models.DateTimeField(null=True,blank=True) #  Fecha del albarán.

class SpecialTaxableEventType(models.Model):
	SpecialTaxableEventCode = models.CharField(max_length=2,choices=SpecialTaxableEventCodeType,null=True,blank=True)
	SpecialTaxableEventReason = models.CharField(max_length=2500,null=True,blank=True) #  Justificación de la fiscalidad especial que se aplica en esta operación. Como este elemento se define a nivel de línea, no de impuesto, es necesario especificar a qué impuesto se refiere. Para establecer esta relación, al comienzo de este elemento se indicará el código del impuesto al que corresponde según la lista de código de impuestos del tipo “TaxTypeCodeType”. Si hubiera varios impuestos con el código “05” (“Otro”), se añadirán los valores de sus campos “TaxRate”, “TaxableBase” y “TaxAmount”, en este orden, hasta que sea posible discernirlos; es decir: 05 [valor “TaxRate”] [valor “TaxableBase”] [valor “TaxAmount”]…

class SubsidyType(models.Model):
	SubsidyDescription = models.CharField(max_length=2500,null=True,blank=True) #  Detalle de la Subvención aplicada.
	SubsidyRate = models.DecimalField(null=True,max_digits=19,decimal_places=10,blank=True) #  Porcentaje de la Subvención. Porcentaje a aplicar al Total Factura. Los porcentajes se reflejan con hasta 8 decimales.
	SubsidyAmount = models.DecimalField(null=True,max_digits=19,decimal_places=10,blank=True) #  Importe de la Subvención. Importe a aplicar al Total Factura. Hasta ocho decimales.

class PaymentOnAccountType(models.Model):
	PaymentOnAccountDate = models.DateTimeField(null=True,blank=True) #  Fecha/s del/os anticipo/s. ISO 8601:2004.
	PaymentOnAccountAmount = models.DecimalField(null=True,max_digits=19,decimal_places=10,blank=True) #  Importe de cada anticipo. Hasta ocho decimales.

class AmountsWithheldType(models.Model):
	WithholdingReason = models.CharField(max_length=2500,null=True,blank=True) #  Motivo de Retención. Descripción de la finalidad de la Retención.
	WithholdingRate = models.DecimalField(null=True,max_digits=19,decimal_places=10,blank=True) #  Porcentaje de Retención. Porcentaje sobre el Total a Pagar. Los porcentajes se reflejan con hasta 8 decimales.
	WithholdingAmount = models.DecimalField(null=True,max_digits=19,decimal_places=10,blank=True) #  Importe de Retención. Importe a retener sobre el Total a Pagar. Hasta ocho decimales.

class LegalLiteralsType(models.Model):
	LegalReference = models.CharField(max_length=250,null=True,blank=True) #  Textos literales que deben figurar obligatoriamente en determinadas facturas. Los textos establecidos en la legislación vigente son: Operación exenta por aplicación del artículo [indicar el artículo] de la Ley 37/1992, de 28 de diciembre, del Impuesto sobre el Valor Añadido; Medio de transporte [describir el medio, por ejemplo automóvil turismo Seat Ibiza TDI 2.0] fecha 1ª puesta en servicio [indicar la fecha] distancias/horas recorridas [indicar la distancia o las horas, por ejemplo, 5.900 km o 48 horas]; Facturación por el destinatario;Inversión del sujeto pasivo; Régimen especial de las agencias de viajes; Régimen especial de los bienes usados; Régimen especial de los objetos de arte; Régimen especial de las antigüedades y objetos de colección; Régimen especial del criterio de caja. NOTA 1: Salvo el texto “Inversión del sujeto pasivo”, los demás se refieren no a la factura en su conjunto, sino a una determinada operación (línea) de la factura. Se deberá especificar a cuál corresponde. NOTA 2: Debe permitirse la posibilidad de cumplimentar este campo con cualquier cadena alfanumérica de hasta 250 caracteres introducida por el usuario por si se establecen nuevos textos literales obligatorios en el futuro.

class AttachmentType(models.Model):
	AttachmentCompressionAlgorithm = models.CharField(max_length=4,choices=AttachmentCompressionAlgorithmType,null=True,blank=True)
	AttachmentFormat = models.CharField(max_length=4,choices=AttachmentFormatType,null=True,blank=True)
	AttachmentEncoding = models.CharField(max_length=6,choices=AttachmentEncodingType,null=True,blank=True)
	AttachmentDescription = models.CharField(max_length=2500,null=True,blank=True) #  Descripción del documento.
	AttachmentData = models.CharField(max_length=40,null=True,blank=True) #  Stream de datos del documento adjunto.

class TaxIdentificationType(models.Model):
	PersonTypeCode = models.CharField(max_length=1,choices=PersonTypeCodeType,null=True,blank=True)
	ResidenceTypeCode = models.CharField(max_length=1,choices=ResidenceTypeCodeType,null=True,blank=True)
	TaxIdentificationNumber = models.CharField(max_length=30,null=True,blank=True) #  Código de Identificación Fiscal del sujeto. Se trata de las composiciones de NIF/CIF que marca la Administración correspondiente (precedidas de las dos letras del país en el caso de operaciones intracomunitarias, es decir, cuando comprador y vendedor tienen domicilio fiscal en estados miembros de la UE distintos).

class RegistrationDataType(models.Model):
	Book = models.CharField(max_length=20,null=True,blank=True) #  Libro.
	RegisterOfCompaniesLocation = models.CharField(max_length=20,null=True,blank=True) #  Registro Mercantil.
	Sheet = models.CharField(max_length=20,null=True,blank=True) #  Hoja.
	Folio = models.CharField(max_length=20,null=True,blank=True) #  Folio.
	Section = models.CharField(max_length=20,null=True,blank=True) #  Sección.
	Volume = models.CharField(max_length=20,null=True,blank=True) #  Tomo.
	AdditionalRegistrationData = models.CharField(max_length=20,null=True,blank=True) #  Otros datos registrales.

class AddressType(models.Model):
	Address = models.CharField(max_length=80,null=True,blank=True) #  Dirección. Tipo de vía, nombre, número, piso…
	PostCode = models.CharField(max_length=5,null=True,blank=True) #  Código Postal asignado por Correos.
	Town = models.CharField(max_length=50,null=True,blank=True) #  Población. Correspondiente al C.P.
	Province = models.CharField(max_length=20,null=True,blank=True) #  Provincia. Donde está situada la Población.
	CountryCode = models.CharField(max_length=3,choices=CountryType,null=True,blank=True)

class OverseasAddressType(models.Model):
	Address = models.CharField(max_length=80,null=True,blank=True) #  Dirección. Tipo de vía, nombre, número, piso....
	PostCodeAndTown = models.CharField(max_length=50,null=True,blank=True) #  Población y Código Postal en el extranjero.
	Province = models.CharField(max_length=20,null=True,blank=True) #  Provincia, Estado, etc.
	CountryCode = models.CharField(max_length=3,choices=CountryType,null=True,blank=True)

class ContactDetailsType(models.Model):
	Telephone = models.CharField(max_length=15,null=True,blank=True) #  Teléfono. Número de teléfono completo con prefijos del país.
	TeleFax = models.CharField(max_length=15,null=True,blank=True) #  Fax. Número de fax completo con prefijos del país.
	WebAddress = models.CharField(max_length=60,null=True,blank=True) #  Página web. URL de la dirección de Internet.
	ElectronicMail = models.CharField(max_length=60,null=True,blank=True) #  Correo electrónico. Dirección de correo electrónico.
	ContactPersons = models.CharField(max_length=40,null=True,blank=True) #  Contactos. Apellidos y Nombre/Razón Social.
	CnoCnae = models.CharField(max_length=5,null=True,blank=True) #  CNO/CNAE. Código Asignado por el INE.
	INETownCode = models.CharField(max_length=9,null=True,blank=True) #  Código de población asignado por el INE.
	AdditionalContactDetails = models.CharField(max_length=60,null=True,blank=True) #  Otros datos de contacto.

class AdministrativeCentreType(models.Model):
	CentreCode = models.CharField(max_length=10,null=True,blank=True) #  Número del Departamento Emisor.
	RoleTypeCode = models.CharField(max_length=2,choices=RoleTypeCodeType,null=True,blank=True)
	Name = models.CharField(max_length=40,null=True,blank=True) #  Nombre de la persona responsable o de relación del centro.
	FirstSurname = models.CharField(max_length=40,null=True,blank=True) #  Primer apellido de la persona responsable o de relación del centro.
	SecondSurname = models.CharField(max_length=40,null=True,blank=True) #  Segundo apellido de la persona responsable o de relación del centro.
	AddressInSpain = models.ForeignKey(AddressType, blank=True, null=True, related_name='address_in_spain_administrative_centre_type_address_type') # Dirección nacional. Dirección en España.
	OverseasAddress = models.ForeignKey(OverseasAddressType, blank=True, null=True, related_name='overseas_address_administrative_centre_type_overseas_address_type') # Dirección en el extranjero.
	ContactDetails = models.ForeignKey(ContactDetailsType, blank=True, null=True, related_name='contact_details_administrative_centre_type_contact_details_type') # Datos de contacto.
	PhysicalGLN = models.CharField(max_length=14,null=True,blank=True) #  GLN Físico. Identificación del punto de conexión a la VAN EDI (Global Location Number). Código de barras de 13 posiciones estándar. Valores registrados por AECOC. Recoge el código de País (2p) España es "84" + Empresa (5p) + los restantes - el último es el producto + dígito de control.
	LogicalOperationalPoint = models.CharField(max_length=14,null=True,blank=True) #  Punto Lógico Operacional. Código identificativo de la Empresa. Código de barras de 13 posiciones estándar. Valores registrados por AECOC. Recoge el código de País (2p) España es "84" + Empresa (5p) + los restantes - el último es el producto + dígito de control.
	CentreDescription = models.CharField(max_length=2500,null=True,blank=True) #  Descripción del centro.

class DiscountType(models.Model):
	DiscountReason = models.CharField(max_length=2500,null=True,blank=True) #  Concepto por el que se aplica descuento.
	DiscountRate = models.DecimalField(null=True,max_digits=19,decimal_places=10,blank=True) #  Porcentaje a descontar del Total Importe Bruto (TIB). Los porcentajes se reflejan con hasta 8 decimales.
	DiscountAmount = models.DecimalField(null=True,max_digits=19,decimal_places=10,blank=True) #  Importe a descontar sobre el TIB. Hasta ocho decimales.

class ChargeType(models.Model):
	ChargeReason = models.CharField(max_length=2500,null=True,blank=True) #  Concepto por el que se aplica el cargo.
	ChargeRate = models.DecimalField(null=True,max_digits=19,decimal_places=10,blank=True) #  Porcentaje a cargar sobre el TIB. Los porcentajes se reflejan con hasta 8 decimales.
	ChargeAmount = models.DecimalField(null=True,max_digits=19,decimal_places=10,blank=True) #  Importe a cargar sobre el TIB. Hasta 8 decimales.

class AmountType(models.Model):
	TotalAmount = models.DecimalField(null=True,max_digits=19,decimal_places=10,blank=True) #  Importe en la moneda original de la facturación. Siempre que la divisa de facturación sea distinta de EURO, el elemento EquivalentInEuros deberá cumplimentarse para satisfacer los requerimientos del Art.10.1 del Reglamento sobre facturación, RD 1496/2003 de 28 de Noviembre.
	EquivalentInEuros = models.DecimalField(null=True,max_digits=19,decimal_places=10,blank=True) #  Importe equivalente en Euros. Siempre con dos decimales.

class AccountType(models.Model):
	IBAN = models.CharField(max_length=34,null=True,blank=True) #  IBAN. Único formato admitido para identificar la cuenta. (Recomendado)
	AccountNumber = models.CharField(max_length=34,null=True,blank=True) #  Número de cuenta.
	BankCode = models.CharField(max_length=60,null=True,blank=True) #  Código de la entidad financiera.
	BranchCode = models.CharField(max_length=60,null=True,blank=True) #  Código de la oficina de la entidad financiera.
	BranchInSpainAddress = models.ForeignKey(AddressType, blank=True, null=True, related_name='branch_in_spain_address_account_type_address_type') # Dirección de la sucursal/oficina en España.
	OverseasBranchAddress = models.ForeignKey(OverseasAddressType, blank=True, null=True, related_name='overseas_branch_address_account_type_overseas_address_type') # Dirección de la sucursal/oficina en el extranjero.
	BIC = models.CharField(max_length=11,null=True,blank=True) #  Código SWIFT. Será obligatorio rellenar las 11 posiciones, utilizando los caracteres XXX cuando no se informe de la sucursal.

class PeriodDates(models.Model):
	StartDate = models.DateTimeField(null=True,blank=True) #  Fecha de inicio. ISO 8601:2004.
	EndDate = models.DateTimeField(null=True,blank=True) #  Fecha final. ISO 8601:2004.

class BatchType(models.Model):
	BatchIdentifier = models.CharField(max_length=70,null=True,blank=True) #  Identificador del lote. Concatenación del nº de documento del emisor con el número de la primera factura y el número de serie caso de existir.
	InvoicesCount = models.BigIntegerField(null=True,blank=True) #  Número total de facturas. Refleja, cuando es lote, el número de facturas del mismo. Siempre será valor "1" cuando el campo Modality (Modalidad) tenga el valor "I".
	TotalInvoicesAmount = models.ForeignKey(AmountType, blank=True, null=True, related_name='total_invoices_amount_batch_type_amount_type') # Total facturas. Suma de los importes InvoiceTotal del Fichero. Este importe lo es a efectos de total de factura y fiscales, sin tener en cuenta subvenciones, anticipos y/o retenciones que pudieran haberse practicado.
	TotalOutstandingAmount = models.ForeignKey(AmountType, blank=True, null=True, related_name='total_outstanding_amount_batch_type_amount_type') # Total a pagar. Suma de los importes TotalOutstandingAmount del Fichero, hasta ocho decimales. Es el importe que efectivamente se adeuda, una vez descontados los anticipos y sin tener en cuenta las retenciones.
	TotalExecutableAmount = models.ForeignKey(AmountType, blank=True, null=True, related_name='total_executable_amount_batch_type_amount_type') # Total a Ejecutar. Sumatorio de las diferencias de los importes (TotalOutstandingAmount y WithholdingAmount) del fichero = Sumatorio de los Importes TotalExecutableAmount, hasta ocho decimales. Es el importe que se adeuda minorado en un posible importe retenido en garantía de cumplimientos contractuales.
	InvoiceCurrencyCode = models.CharField(max_length=3,choices=CurrencyCodeType,null=True,blank=True)

class InvoiceIssueDataType(models.Model):
	IssueDate = models.DateTimeField(null=True,blank=True) #  Fecha de expedición. Fecha en la que se genera la factura con efectos fiscales. ISO 8601:2004. Esta fecha no podrá ser posterior a la fecha de la firma electrónica.
	OperationDate = models.DateTimeField(null=True,blank=True) #  Fecha de Operación. Fecha en la que se realiza el servicio o se entrega el bien. ISO 8601:2004. Esta fecha solo será obligatoria si es distinta de la fecha de expedición.
	PlaceOfIssue = models.ForeignKey(PlaceOfIssueType, blank=True, null=True, related_name='place_of_issue_invoice_issue_data_type_place_of_issue_type') # Lugar de expedición. Plaza en la que se expide el documento.
	InvoicingPeriod = models.ForeignKey(PeriodDates, blank=True, null=True, related_name='invoicing_period_invoice_issue_data_type_period_dates') # Periodo de facturación. Sólo cuando se requiera: Servicio prestado temporalmente o Factura Recapitulativa. Esta información será obligatoria cuando el dato InvoiceClass (Clase) contenga alguno de los valores: "OC" ó "CC". ISO 8601:2004.
	InvoiceCurrencyCode = models.CharField(max_length=3,choices=CurrencyCodeType,null=True,blank=True)
	ExchangeRateDetails = models.ForeignKey(ExchangeRateDetailsType, blank=True, null=True, related_name='exchange_rate_details_invoice_issue_data_type_exchange_rate_details_type') # Detalles del tipo de cambio.
	TaxCurrencyCode = models.CharField(max_length=3,choices=CurrencyCodeType,null=True,blank=True)
	LanguageName = models.CharField(max_length=2,choices=LanguageCodeType,null=True,blank=True)

class CorrectiveType(models.Model):
	InvoiceNumber = models.CharField(max_length=20,null=True,blank=True) #  Número de la factura que se rectifica. Será obligatorio cuando el dato "CorrectionMethod" (Código del criterio de la rectificación) sea "01" o "02".
	InvoiceSeriesCode = models.CharField(max_length=20,null=True,blank=True) #  Número de serie de la factura que se rectifica.
	ReasonCode = models.CharField(max_length=2,choices=ReasonCodeType,null=True,blank=True)
	ReasonDescription = models.CharField(max_length=93,choices=ReasonDescriptionType,null=True,blank=True)
	TaxPeriod = models.ForeignKey(PeriodDates, blank=True, null=True, related_name='tax_period_corrective_type_period_dates') # Período natural en el que se produjeron los efectos fiscales de la factura a rectificar; y, por lo tanto, se tributó, y que ahora, es objeto de rectificación. ISO 8601:2004.
	CorrectionMethod = models.CharField(max_length=2,choices=CorrectionMethodType,null=True,blank=True)
	CorrectionMethodDescription = models.CharField(max_length=73,choices=CorrectionMethodDescriptionType,null=True,blank=True)
	AdditionalReasonDescription = models.CharField(max_length=2500,null=True,blank=True) #  Ampliación motivo de la rectificación. Descripción de las aclaraciones y motivos de la factura rectificativa.

class DeliveryNotesReferencesType(models.Model):
	DeliveryNote = models.ForeignKey(DeliveryNoteType, blank=True, null=True, related_name='delivery_note_delivery_notes_references_type_delivery_note_type') # Información del albarán.

class SubsidiesType(models.Model):
	Subsidy = models.ForeignKey(SubsidyType, blank=True, null=True, related_name='subsidy_subsidies_type_subsidy_type') # Subvención.

class PaymentsOnAccountType(models.Model):
	PaymentOnAccount = models.ForeignKey(PaymentOnAccountType, blank=True, null=True, related_name='payment_on_account_payments_on_account_type_payment_on_account_type') # Anticipo.

class ReimbursableExpensesType(models.Model):
	ReimbursableExpensesSellerParty = models.ForeignKey(TaxIdentificationType, blank=True, null=True, related_name='reimbursable_expenses_seller_party_reimbursable_expenses_type_tax_identification_type')
	ReimbursableExpensesBuyerParty = models.ForeignKey(TaxIdentificationType, blank=True, null=True, related_name='reimbursable_expenses_buyer_party_reimbursable_expenses_type_tax_identification_type')
	IssueDate = models.DateTimeField(null=True,blank=True)
	InvoiceNumber = models.CharField(max_length=20,null=True,blank=True)
	InvoiceSeriesCode = models.CharField(max_length=20,null=True,blank=True)
	ReimbursableExpensesAmount = models.DecimalField(null=True,max_digits=19,decimal_places=10,blank=True)

class InstallmentType(models.Model):
	InstallmentDueDate = models.DateTimeField(null=True,blank=True) #  Fechas en las que se deben atender los pagos. ISO 8601:2004.
	InstallmentAmount = models.DecimalField(null=True,max_digits=19,decimal_places=10,blank=True) #  Importe a satisfacer en cada plazo. Siempre con dos decimales.
	PaymentMeans = models.CharField(max_length=2,choices=PaymentMeansType,null=True,blank=True)
	AccountToBeCredited = models.ForeignKey(AccountType, blank=True, null=True, related_name='account_to_be_credited_installment_type_account_type') # Cuenta de abono. Único formato admitido. Cuando la forma de pago (PaymentMeans) sea "transferencia" este dato será obligatorio.
	PaymentReconciliationReference = models.CharField(max_length=60,null=True,blank=True) #  Referencia expresa del pago. Dato que precisa el Emisor para conciliar los pagos con cada factura.
	AccountToBeDebited = models.ForeignKey(AccountType, blank=True, null=True, related_name='account_to_be_debited_installment_type_account_type') # Cuenta de cargo. Único formato admitido. Cuando la forma de pago (PaymentMeans) sea "recibo domiciliado" este dato será obligatorio.
	CollectionAdditionalInformation = models.CharField(max_length=2500,null=True,blank=True) #  Observaciones de cobro. Libre para uso del Emisor.
	RegulatoryReportingData = models.CharField(max_length=6,null=True,blank=True) #  Código Estadístico. Usado en las operaciones transfronterizas según las especificaciones de la circular del Banco España 15/1992
	DebitReconciliationReference = models.CharField(max_length=60,null=True,blank=True) #  Referencia del cliente pagador, similar a la utilizada por elemisor para la conciliación de los pagos.

class AttachedDocumentsType(models.Model):
	Attachment = models.ForeignKey(AttachmentType, blank=True, null=True, related_name='attachment_attached_documents_type_attachment_type') # Documento adjunto. En [BASE-64]. Contiene los documentos relacionados con la factura en el formato deseado (imagen, PDF, XML, etc.)

class LegalEntityType(models.Model):
	CorporateName = models.CharField(max_length=80,null=True,blank=True) #  Razón Social.
	TradeName = models.CharField(max_length=40,null=True,blank=True) #  Nombre Comercial.
	RegistrationData = models.ForeignKey(RegistrationDataType, blank=True, null=True, related_name='registration_data_legal_entity_type_registration_data_type') # Datos Registrales: Inscripción Registro, Tomo, Folio,…
	AddressInSpain = models.ForeignKey(AddressType, blank=True, null=True, related_name='address_in_spain_legal_entity_type_address_type') # Dirección Nacional. Dirección en España.
	OverseasAddress = models.ForeignKey(OverseasAddressType, blank=True, null=True, related_name='overseas_address_legal_entity_type_overseas_address_type') # Dirección en el extranjero.
	ContactDetails = models.ForeignKey(ContactDetailsType, blank=True, null=True, related_name='contact_details_legal_entity_type_contact_details_type') # Datos de contacto.

class IndividualType(models.Model):
	Name = models.CharField(max_length=40,null=True,blank=True) #  Nombre de la persona física.
	FirstSurname = models.CharField(max_length=40,null=True,blank=True) #  Primer apellido de la persona física.
	SecondSurname = models.CharField(max_length=40,null=True,blank=True) #  Segundo apellido de la persona física.
	AddressInSpain = models.ForeignKey(AddressType, blank=True, null=True, related_name='address_in_spain_individual_type_address_type') # Dirección nacional. Dirección en España.
	OverseasAddress = models.ForeignKey(OverseasAddressType, blank=True, null=True, related_name='overseas_address_individual_type_overseas_address_type') # Dirección en el extranjero.
	ContactDetails = models.ForeignKey(ContactDetailsType, blank=True, null=True, related_name='contact_details_individual_type_contact_details_type') # Datos de contacto.

class AdministrativeCentresType(models.Model):
	AdministrativeCentre = models.ForeignKey(AdministrativeCentreType, blank=True, null=True, related_name='administrative_centre_administrative_centres_type_administrative_centre_type') # Centro.

class DiscountsAndRebatesType(models.Model):
	Discount = models.ForeignKey(DiscountType, blank=True, null=True, related_name='discount_discounts_and_rebates_type_discount_type') # Descuento.

class ChargesType(models.Model):
	Charge = models.ForeignKey(ChargeType, blank=True, null=True, related_name='charge_charges_type_charge_type') # Cargo.

class TaxType(models.Model):
	TaxTypeCode = models.CharField(max_length=2,choices=TaxTypeCodeType,null=True,blank=True)
	TaxRate = models.DecimalField(null=True,max_digits=19,decimal_places=10,blank=True) #  Tipo impositivo. Hasta ocho decimales.
	TaxableBase = models.ForeignKey(AmountType, blank=True, null=True, related_name='taxable_base_tax_type_amount_type') # Base de retención. Hasta ocho decimales.
	TaxAmount = models.ForeignKey(AmountType, blank=True, null=True, related_name='tax_amount_tax_type_amount_type') # Importe de la retención. Siempre con dos decimales.

class TaxOutputType(models.Model):
	TaxTypeCode = models.CharField(max_length=2,choices=TaxTypeCodeType,null=True,blank=True)
	TaxRate = models.DecimalField(null=True,max_digits=19,decimal_places=10,blank=True) #  Tipo impositivo. Téngase en cuenta que no siempre son porcentajes. La legislación del impuesto correspondiente permitirá identificar las unidades y dimensiones del tipo impositivo. Hasta ocho decimales.
	TaxableBase = models.ForeignKey(AmountType, blank=True, null=True, related_name='taxable_base_tax_output_type_amount_type') # Base imponible. La legislación del impuesto correspondiente determina cómo se calcula la base imponible.Hasta ocho decimales.
	TaxAmount = models.ForeignKey(AmountType, blank=True, null=True, related_name='tax_amount_tax_output_type_amount_type') # Cuota. La legislación del impuesto correspondiente determina cómo se calcula la cuota. Hasta ocho decimales.
	SpecialTaxableBase = models.ForeignKey(AmountType, blank=True, null=True, related_name='special_taxable_base_tax_output_type_amount_type') # Base imponible del régimen especial del grupo de entidades (Arts. 163 quinquies a 163 nonies de la Ley 37/1992, de 28 de diciembre, del IVA). En el caso de aplicar el régimen especial habrán de consignar en factura no sólo la base conforme al coste de adquisición de los bienes y servicios sino, además, la base que hubiera correspondido tener en cuenta de no aplicarse el régimen especial. Es decir: deben consignarse dos bases distintas para la misma operación aunque el cálculo de la cuota sólo debe efectuarse respecto de la base imponible del régimen especial. En el caso en el que se expida factura con repercusión del impuesto a pesar de tratarse de una de las operaciones exentas de las reguladas en el artículo 20.Uno de la Ley 37/1992, de 28 de diciembre, se tiene que especificar que se está repercutiendo el impuesto porque se ha renunciado a la exención tal y como habilita el artículo 163.sexies.Cinco de la Ley del impuesto. Esto se indicará en el elemento “AdditionalLineItemInformation” con la siguiente expresión: “Renuncia a la exención en virtud artículo 163.sexies.Cinco de la Ley 37/1992”. Hasta ocho decimales.
	SpecialTaxAmount = models.ForeignKey(AmountType, blank=True, null=True, related_name='special_tax_amount_tax_output_type_amount_type') # Cuota especial. Importe resultante de aplicar el tipo de gravamen sobre la base imponible del régimen especial del grupo de entidades. Hasta ocho decimales.
	EquivalenceSurcharge = models.DecimalField(null=True,max_digits=19,decimal_places=10,blank=True) #  Tipo de recargo de Equivalencia. Siempre con dos decimales.
	EquivalenceSurchargeAmount = models.ForeignKey(AmountType, blank=True, null=True, related_name='equivalence_surcharge_amount_tax_output_type_amount_type') # Cuota. Importe resultante de aplicar a la Base Imponible, la misma que para el IVA, el porcentaje indicado en “EquivalenceSurchage”. Hasta ocho decimales.

class ThirdPartyType(models.Model):
	TaxIdentification = models.ForeignKey(TaxIdentificationType, blank=True, null=True, related_name='tax_identification_third_party_type_tax_identification_type') # Identificación fiscal.
	LegalEntity = models.ForeignKey(LegalEntityType, blank=True, null=True, related_name='legal_entity_third_party_type_legal_entity_type') # Persona jurídica y otras.
	Individual = models.ForeignKey(IndividualType, blank=True, null=True, related_name='individual_third_party_type_individual_type') # Persona física.

class AssigneeType(models.Model):
	TaxIdentification = models.ForeignKey(TaxIdentificationType, blank=True, null=True, related_name='tax_identification_assignee_type_tax_identification_type') # Identificación fiscal.
	LegalEntity = models.ForeignKey(LegalEntityType, blank=True, null=True, related_name='legal_entity_assignee_type_legal_entity_type') # Persona jurídica y otras.
	Individual = models.ForeignKey(IndividualType, blank=True, null=True, related_name='individual_assignee_type_individual_type') # Persona física.

class BusinessType(models.Model):
	TaxIdentification = models.ForeignKey(TaxIdentificationType, blank=True, null=True, related_name='tax_identification_business_type_tax_identification_type') # Identificación fiscal.
	PartyIdentification = models.CharField(max_length=10,null=True,blank=True) #  Identificación de la entidad; Rellenar con el número de referencia de la entidad del programa de facturación que utilice.
	AdministrativeCentres = models.ForeignKey(AdministrativeCentresType, blank=True, null=True, related_name='administrative_centres_business_type_administrative_centres_type') # Centros.
	LegalEntity = models.ForeignKey(LegalEntityType, blank=True, null=True, related_name='legal_entity_business_type_legal_entity_type') # Persona jurídica y otras.
	Individual = models.ForeignKey(IndividualType, blank=True, null=True, related_name='individual_business_type_individual_type') # Persona física.

class InvoiceHeaderType(models.Model):
	InvoiceNumber = models.CharField(max_length=20,null=True,blank=True) #  Número de factura. Número asignado por el Emisor.
	InvoiceSeriesCode = models.CharField(max_length=20,null=True,blank=True) #  Número de serie asignado por el Emisor.
	InvoiceDocumentType = models.CharField(max_length=2,choices=InvoiceDocumentTypeType,null=True,blank=True)
	InvoiceClass = models.CharField(max_length=2,choices=InvoiceClassType,null=True,blank=True)
	Corrective = models.ForeignKey(CorrectiveType, blank=True, null=True, related_name='corrective_invoice_header_type_corrective_type') # Rectificativa.

class ReimbursableExpenses(models.Model):
	ReimbursableExpenses = models.ForeignKey(ReimbursableExpensesType, blank=True, null=True, related_name='reimbursable_expenses_reimbursable_expenses_reimbursable_expenses_type') # Suplidos.

class InstallmentsType(models.Model):
	Installment = models.ForeignKey(InstallmentType, blank=True, null=True, related_name='installment_installments_type_installment_type') # Vencimiento.

class AdditionalDataType(models.Model):
	RelatedInvoice = models.CharField(max_length=40,null=True,blank=True) #  Factura asociada. Número y Serie de acuerdo Emisor/Receptor.
	RelatedDocuments = models.ForeignKey(AttachedDocumentsType, blank=True, null=True, related_name='related_documents_additional_data_type_attached_documents_type') # Documentos asociados. Identificación de documentos Emisor/Receptor.
	InvoiceAdditionalInformation = models.CharField(max_length=2500,null=True,blank=True) #  Información adicional. Lo que considere oportuno el Emisor. En este elemento se recogerá el motivo por lo que el impuesto correspondiente está "no sujeto" o "exento", cuando se produzca esta situación.

class TaxesType(models.Model):
	Tax = models.ForeignKey(TaxType, blank=True, null=True, related_name='tax_taxes_type_tax_type') # Impuesto.

class FactoringAssignmentDataType(models.Model):
	Assignee = models.ForeignKey(AssigneeType, blank=True, null=True, related_name='assignee_factoring_assignment_data_type_assignee_type') # Cesionario.
	PaymentDetails = models.ForeignKey(InstallmentsType, blank=True, null=True, related_name='payment_details_factoring_assignment_data_type_installments_type') # Datos de pago.
	FactoringAssignmentClauses = models.CharField(max_length=2500,null=True,blank=True) #  Texto de la cláusula de cesión.

class PartiesType(models.Model):
	SellerParty = models.ForeignKey(BusinessType, blank=True, null=True, related_name='seller_party_parties_type_business_type') # Emisor. Datos básicos del fichero. Son comunes a la factura o facturas que se incluyen.
	BuyerParty = models.ForeignKey(BusinessType, blank=True, null=True, related_name='buyer_party_parties_type_business_type') # Receptor. Datos básicos del fichero. Son comunes a la factura o facturas que se incluyen.

class InvoiceLineType(models.Model):
	IssuerContractReference = models.CharField(max_length=20,null=True,blank=True) #  Referencia del contrato del Emisor.
	IssuerContractDate = models.DateTimeField(null=True,blank=True) #  Fecha del contrato del emisor.
	IssuerTransactionReference = models.CharField(max_length=20,null=True,blank=True) #  Referencia de la Operación, Número de Pedido, Contrato, etc. del Emisor.
	IssuerTransactionDate = models.DateTimeField(null=True,blank=True) #  Fecha de operación / pedido del emisor.
	ReceiverContractReference = models.CharField(max_length=20,null=True,blank=True) #  Referencia del contrato del Receptor.
	ReceiverContractDate = models.DateTimeField(null=True,blank=True) #  Fecha del contrato del receptor.
	ReceiverTransactionReference = models.CharField(max_length=20,null=True,blank=True) #  Referencia de la Operación, Número de Pedido, Contrato, etc. del Receptor.
	ReceiverTransactionDate = models.DateTimeField(null=True,blank=True) #  Fecha de operación / pedido del receptor.
	FileReference = models.CharField(max_length=20,null=True,blank=True) #  Referencia del expediente.
	FileDate = models.DateTimeField(null=True,blank=True) #  Fecha del expediente.
	SequenceNumber = models.DecimalField(null=True,max_digits=19,decimal_places=10,blank=True) #  Número de secuencia o línea del pedido.
	DeliveryNotesReferences = models.ForeignKey(DeliveryNotesReferencesType, blank=True, null=True, related_name='delivery_notes_references_invoice_line_type_delivery_notes_references_type') # Referencias de albaranes.
	ItemDescription = models.CharField(max_length=2500,null=True,blank=True) #  Descripción del bien o servicio.
	Quantity = models.DecimalField(null=True,max_digits=19,decimal_places=10,blank=True) #  Cantidad. Número de Unidades servidas/prestadas.
	UnitOfMeasure = models.CharField(max_length=2,choices=UnitOfMeasureType,null=True,blank=True)
	UnitPriceWithoutTax = models.DecimalField(null=True,max_digits=19,decimal_places=10,blank=True) #  Precio de la unidad de bien o servicio servido/prestado, en la moneda indicada en la Cabecera de la Factura. Siempre sin Impuestos. Hasta ocho decimales.
	TotalCost = models.DecimalField(null=True,max_digits=19,decimal_places=10,blank=True) #  Coste Total. Resultado: Quantity x UnitPriceWithoutTax. Hasta ocho decimales.
	DiscountsAndRebates = models.ForeignKey(DiscountsAndRebatesType, blank=True, null=True, related_name='discounts_and_rebates_invoice_line_type_discounts_and_rebates_type') # Descuentos.
	Charges = models.ForeignKey(ChargesType, blank=True, null=True, related_name='charges_invoice_line_type_charges_type') # Cargos.
	GrossAmount = models.DecimalField(null=True,max_digits=19,decimal_places=10,blank=True) #  Importe bruto. Resultado: TotalCost - DiscountAmount + ChargeAmount. Hasta ocho decimales.
	TaxesWithheld = models.ForeignKey(TaxesType, blank=True, null=True, related_name='taxes_withheld_invoice_line_type_taxes_type') # Impuestos retenidos. Es una secuencia de elementos, cada uno de los cuales contiene la información de un impuesto retenido.
	TaxesOutputs = models.ForeignKey(TaxOutputType, blank=True, null=True, related_name='taxes_outputs_invoice_line_type_tax_output_type') # Impuestos repercutidos. Es una secuencia de elementos, cada uno de los cuales contiene la información de un impuesto repercutido.
	LineItemPeriod = models.ForeignKey(PeriodDates, blank=True, null=True, related_name='line_item_period_invoice_line_type_period_dates') # Información sobre el periodo de prestación de un servicio. ISO 8601 :2004.
	TransactionDate = models.DateTimeField(null=True,blank=True) #  Fecha concreta de prestación o entrega del bien o servicio. ISO 8601:2004.
	AdditionalLineItemInformation = models.CharField(max_length=2500,null=True,blank=True) #  Información adicional. Libre para el emisor por cada detalle.
	SpecialTaxableEvent = models.ForeignKey(SpecialTaxableEventType, blank=True, null=True, related_name='special_taxable_event_invoice_line_type_special_taxable_event_type') # Este campo indica la obligatoriedad de los impuestos.
	ArticleCode = models.CharField(max_length=20,null=True,blank=True) #  Código de artículo.


class InvoiceTotalsType(models.Model):
	TotalGrossAmount = models.DecimalField(null=True,max_digits=19,decimal_places=10,blank=True) #  Total Importe Bruto. Suma total de importes brutos de los detalles de la factura. Hasta ocho decimales.
	GeneralDiscounts = models.ForeignKey(DiscountsAndRebatesType, blank=True, null=True, related_name='general_discounts_invoice_totals_type_discounts_and_rebates_type') # Descuentos sobre el Total Importe Bruto. Habrá tantos bloques de campos GeneralDiscounts como clases de descuentos diferentes se apliquen a nivel de factura.
	GeneralSurcharges = models.ForeignKey(ChargesType, blank=True, null=True, related_name='general_surcharges_invoice_totals_type_charges_type') # Cargos sobre el Total Importe Bruto. Habrá tantos bloques de campos GeneralSurcharges como clases de cargos/recargos se apliquen, a nivel de factura.
	TotalGeneralDiscounts = models.DecimalField(null=True,max_digits=19,decimal_places=10,blank=True) #  Total general de descuentos. Sumatorio de los importes de los diferentes campos GeneralDiscounts. Hasta ocho decimales.
	TotalGeneralSurcharges = models.DecimalField(null=True,max_digits=19,decimal_places=10,blank=True) #  Total general de cargos. Sumatorio de los importes de los diferentes campos GeneralSurcharges. Hasta ocho decimales
	TotalGrossAmountBeforeTaxes = models.DecimalField(null=True,max_digits=19,decimal_places=10,blank=True) #  Total importe bruto antes de impuestos. Resultado de: TotalGrossAmount - TotalGeneralDiscounts + TotalGeneralSurcharges. Hasta ocho decimales.
	TotalTaxOutputs = models.DecimalField(null=True,max_digits=19,decimal_places=10,blank=True) #  Total impuestos repercutidos. Sumatorio de todas Cuotas y Recargos de Equivalencia. Hasta ocho decimales.
	TotalTaxesWithheld = models.DecimalField(null=True,max_digits=19,decimal_places=10,blank=True) #  Total impuestos retenidos. Hasta ocho decimales.
	InvoiceTotal = models.DecimalField(null=True,max_digits=19,decimal_places=10,blank=True) #  Total factura. Resultado de: TotalGrossAmountBeforeTaxes + TotalTaxOutputs - TotalTaxesWithheld. Hasta ocho decimales.
	Subsidies = models.ForeignKey(SubsidiesType, blank=True, null=True, related_name='subsidies_invoice_totals_type_subsidies_type') # Subvenciones por adquisición de determinados bienes. Habrá tantos bloques de campos Subsidies como subvenciones se apliquen. En el caso de que la subvención se aplique solo a parte de las operaciones facturadas, en el subelemento SubsidyDescription se especificará también a qué operación corresponde.
	PaymentsOnAccount = models.ForeignKey(PaymentsOnAccountType, blank=True, null=True, related_name='payments_on_account_invoice_totals_type_payments_on_account_type') # Anticipos. Pagos anticipados sobre el Total Facturas. Habrá tantos bloques PaymentsOnAccount como clases de anticipos se apliquen a nivel factura.
	ReimbursableExpenses = models.ForeignKey(ReimbursableExpenses, blank=True, null=True, related_name='reimbursable_expenses_invoice_totals_type_reimbursable_expenses') # Suplidos incorporados en la factura.
	TotalFinancialExpenses = models.DecimalField(null=True,max_digits=19,decimal_places=10,blank=True) #  Total de gastos financieros. Siempre con dos decimales.
	TotalOutstandingAmount = models.DecimalField(null=True,max_digits=19,decimal_places=10,blank=True) #  Total a pagar. Resultado de: InvoiceTotal - (Total subvenciones + TotalPaymentsOnAccount). En Total subvenciones se suman las cantidades especificadas en los bloques Subsidies. Hasta ocho decimales.
	TotalPaymentsOnAccount = models.DecimalField(null=True,max_digits=19,decimal_places=10,blank=True) #  Total de anticipos. Sumatorio de los campos PaymentOnAccountAmount. Hasta ocho decimales.
	AmountsWithheld = models.ForeignKey(AmountsWithheldType, blank=True, null=True, related_name='amounts_withheld_invoice_totals_type_amounts_withheld_type') # Cantidades que retiene el pagador hasta el buen fin de la operación.
	TotalExecutableAmount = models.DecimalField(null=True,max_digits=19,decimal_places=10,blank=True) #  Total a ejecutar. Resultado de: TotalOutstandingAmount - Total de Cantidades retenidas + TotalReimbursableExpenses  + TotalFinancialExpenses. En Total de Cantidades retenidas se sumaran las cantidades especificadas en los bloques AmountsWithheld. Hasta ocho decimales.
	TotalReimbursableExpenses = models.DecimalField(null=True,max_digits=19,decimal_places=10,blank=True) #  Total de suplidos. Hasta ocho decimales.

class FileHeaderType(models.Model):
	SchemaVersion = models.CharField(default='3.2.1',max_length=5,null=True,blank=True)
	Modality = models.CharField(max_length=1,choices=ModalityType,null=True,blank=True)
	InvoiceIssuerType = models.CharField(max_length=2,choices=InvoiceIssuerTypeType,null=True,blank=True)
	ThirdParty = models.ForeignKey(ThirdPartyType, blank=True, null=True, related_name='third_party_file_header_type_third_party_type') # Tercero. La factura puede ser generada y firmada por un Tercero.
	Batch = models.ForeignKey(BatchType, blank=True, null=True, related_name='batch_file_header_type_batch_type') # Lote.
	FactoringAssignmentData = models.ForeignKey(FactoringAssignmentDataType, blank=True, null=True, related_name='factoring_assignment_data_file_header_type_factoring_assignment_data_type') # Datos cesión factoring.

class ItemsType(models.Model):
	InvoiceLine = models.ForeignKey(InvoiceLineType, blank=True, null=True, related_name='invoice_line_items_type_invoice_line_type') # Lineas de detalle de la factura.

class InvoiceType(models.Model):
	InvoiceHeader = models.ForeignKey(InvoiceHeaderType, blank=True, null=True, related_name='invoice_header_invoice_type_invoice_header_type') # Cabecera de factura. Para cada una de las facturas que pueden componer un Lote, recoge datos que determinan inequívocamente cada factura.
	InvoiceIssueData = models.ForeignKey(InvoiceIssueDataType, blank=True, null=True, related_name='invoice_issue_data_invoice_type_invoice_issue_data_type') # Datos de la emisión de la factura.
	TaxesOutputs = models.ForeignKey(TaxOutputType, blank=True, null=True, related_name='taxes_outputs_invoice_type_tax_output_type') # Impuestos repercutidos.
	TaxesWithheld = models.ForeignKey(TaxesType, blank=True, null=True, related_name='taxes_withheld_invoice_type_taxes_type') # Impuestos retenidos.
	InvoiceTotals = models.ForeignKey(InvoiceTotalsType, blank=True, null=True, related_name='invoice_totals_invoice_type_invoice_totals_type') # Totales de factura.
	Items = models.ForeignKey(ItemsType, blank=True, null=True, related_name='items_invoice_type_items_type') # Información detallada.
	PaymentDetails = models.ForeignKey(InstallmentsType, blank=True, null=True, related_name='payment_details_invoice_type_installments_type') # Datos de pago.
	LegalLiterals = models.ForeignKey(LegalLiteralsType, blank=True, null=True, related_name='legal_literals_invoice_type_legal_literals_type') # Literales legales.
	AdditionalData = models.ForeignKey(AdditionalDataType, blank=True, null=True, related_name='additional_data_invoice_type_additional_data_type') # Datos adicionales.

class InvoicesType(models.Model):
	Invoice = models.ForeignKey(InvoiceType, blank=True, null=True, related_name='invoice_invoices_type_invoice_type') # Factura.

class EFactura(models.Model):
    FileHeader = models.ForeignKey(FileHeaderType,
                                   related_name='file_header_e_factura_file_header_type')  # Cabecera del fichero xml
    Parties = models.ForeignKey(PartiesType,
                                related_name='parties_e_factura_parties_type')  # Sujetos - Datos del emisor y receptor de la factura
    Invoices = models.ForeignKey(InvoicesType,
                                 related_name='invoices_e_factura_invoice_type')  # Conjunto de facturas que contiene el fichero. Conjunto de facturas que contiene el fichero. Para todos los elementos numéricos, los cálculos se efectuarán siempre redondeando al número de decimales correspondientes.
    Owner = models.ForeignKey(User, related_name='user') # Usuario
    CreateAt = models.DateTimeField(auto_now_add=True) # Fecha de Creación
