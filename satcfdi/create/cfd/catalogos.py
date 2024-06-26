from enum import StrEnum


class FormaPago(StrEnum):
    EFECTIVO = '01'
    CHEQUE_NOMINATIVO = '02'
    TRANSFERENCIA_ELECTRONICA_DE_FONDOS = '03'
    TARJETA_DE_CREDITO = '04'
    MONEDERO_ELECTRONICO = '05'
    DINERO_ELECTRONICO = '06'
    TAREJTAS_DIGITALES = '07'
    VALES_DE_DESPENSA = '08'
    BIENES = '09'
    SERVICIO = '10'
    POR_CUENTA_DE_TERCERO = '11'
    DACION_EN_PAGO = '12'
    PAGO_POR_SUBROGACION = '13'
    PAGO_POR_CONSIGNACION = '14'
    CONDONACION = '15'
    CANCELACION = '16'
    COMPENSACION = '17'
    NOVACION = '23'
    CONFUSION = '24'
    REMISION_DE_DEUDA = '25'
    PRESCRIPCION_O_CADUCIDAD = '26'
    A_SATISFACCION_DEL_ACREEDOR = '27'
    TARJETA_DE_DEBITO = '28'
    TARJETA_DE_SERVICIOS = '29'
    APLICACION_DE_ANTICIPOS = '30'
    INTERMEDIARIO_PAGOS = '31'
    NA = '98'
    POR_DEFINIR = '99'


class Impuesto(StrEnum):
    ISR = '001'
    IVA = '002'
    IEPS = '003'


class MetodoPago(StrEnum):
    PAGO_EN_PARCIALIDADES_O_DIFERIDO = 'PPD'
    PAGO_EN_UNA_SOLA_EXHIBICION = 'PUE'


class RegimenFiscal(StrEnum):
    GENERAL_DE_LEY_PERSONAS_MORALES = '601'
    PERSONAS_MORALES_CON_FINES_NO_LUCRATIVOS = '603'
    SUELDOS_Y_SALARIOS_E_INGRESOS_ASIMILADOS_A_SALARIOS = '605'
    ARRENDAMIENTO = '606'
    REGIMEN_DE_ENAJENACION_O_ADQUISICION_DE_BIENES = '607'
    DEMAS_INGRESOS = '608'
    CONSOLIDACION = '609'
    RESIDENTES_EN_EL_EXTRANJERO_SIN_ESTABLECIMIENTO_PERMANENTE_EN_MEXICO = '610'
    INGRESOS_POR_DIVIDENDOS_SOCIOS_Y_ACCIONISTAS = '611'
    PERSONAS_FISICAS_CON_ACTIVIDADES_EMPRESARIALES_Y_PROFESIONALES = '612'
    INGRESOS_POR_INTERESES = '614'
    REGIMEN_DE_LOS_INGRESOS_POR_OBTENCION_DE_PREMIOS = '615'
    SIN_OBLIGACIONES_FISCALES = '616'
    SOCIEDADES_COOPERATIVAS_DE_PRODUCCION_QUE_OPTAN_POR_DIFERIR_SUS_INGRESOS = '620'
    INCORPORACION_FISCAL = '621'
    ACTIVIDADES_AGRICOLAS_GANADERAS_SILVICOLAS_Y_PESQUERAS = '622'
    OPCIONAL_PARA_GRUPOS_DE_SOCIEDADES = '623'
    COORDINADOS = '624'
    REGIMEN_DE_LAS_ACTIVIDADES_EMPRESARIALES_CON_INGRESOS_A_TRAVES_DE_PLATAFORMAS_TECNOLOGICAS = '625'
    REGIMEN_SIMPLIFICADO_DE_CONFIANZA = '626'
    HIDROCARBUROS = '628'
    DE_LOS_REGIMENES_FISCALES_PREFERENTES_Y_DE_LAS_EMPRESAS_MULTINACIONALES = '629'
    ENAJENACION_DE_ACCIONES_EN_BOLSA_DE_VALORES = '630'


class TipoDeComprobante(StrEnum):
    EGRESO = 'E'
    INGRESO = 'I'
    NOMINA = 'N'
    PAGO = 'P'
    TRASLADO = 'T'


class TipoFactor(StrEnum):
    CUOTA = 'Cuota'
    EXENTO = 'Exento'
    TASA = 'Tasa'


class TipoRelacion(StrEnum):
    NOTA_DE_CREDITO_DE_LOS_DOCUMENTOS_RELACIONADOS = '01'
    NOTA_DE_DEBITO_DE_LOS_DOCUMENTOS_RELACIONADOS = '02'
    DEVOLUCION_DE_MERCANCIA_SOBRE_FACTURAS_O_TRASLADOS_PREVIOS = '03'
    SUSTITUCION_DE_LOS_CFDI_PREVIOS = '04'
    TRASLADOS_DE_MERCANCIAS_FACTURADOS_PREVIAMENTE = '05'
    FACTURA_GENERADA_POR_LOS_TRASLADOS_PREVIOS = '06'
    CFDI_POR_APLICACION_DE_ANTICIPO = '07'
    FACTURA_GENERADA_POR_PAGOS_EN_PARCIALIDADES = '08'
    FACTURA_GENERADA_POR_PAGOS_DIFERIDOS = '09'


class UsoCFDI(StrEnum):
    NOMINA = 'CN01'
    PAGOS = 'CP01'
    HONORARIOS_MEDICOS_DENTALES_Y_GASTOS_HOSPITALARIOS = 'D01'
    GASTOS_MEDICOS_POR_INCAPACIDAD_O_DISCAPACIDAD = 'D02'
    GASTOS_FUNERALES = 'D03'
    DONATIVOS = 'D04'
    INTERESES_REALES_EFECTIVAMENTE_PAGADOS_POR_CREDITOS_HIPOTECARIOS_CASA_HABITACION = 'D05'
    APORTACIONES_VOLUNTARIAS_AL_SAR = 'D06'
    PRIMAS_POR_SEGUROS_DE_GASTOS_MEDICOS = 'D07'
    GASTOS_DE_TRANSPORTACION_ESCOLAR_OBLIGATORIA = 'D08'
    DEPOSITOS_EN_CUENTAS_PARA_EL_AHORRO_PRIMAS_QUE_TENGAN_COMO_BASE_PLANES_DE_PENSIONES = 'D09'
    PAGOS_POR_SERVICIOS_EDUCATIVOS_COLEGIATURAS = 'D10'
    ADQUISICION_DE_MERCANCIAS = 'G01'
    DEVOLUCIONES_DESCUENTOS_O_BONIFICACIONES = 'G02'
    GASTOS_EN_GENERAL = 'G03'
    CONSTRUCCIONES = 'I01'
    MOBILIARIO_Y_EQUIPO_DE_OFICINA_POR_INVERSIONES = 'I02'
    EQUIPO_DE_TRANSPORTE = 'I03'
    EQUIPO_DE_COMPUTO_Y_ACCESORIOS = 'I04'
    DADOS_TROQUELES_MOLDES_MATRICES_Y_HERRAMENTAL = 'I05'
    COMUNICACIONES_TELEFONICAS = 'I06'
    COMUNICACIONES_SATELITALES = 'I07'
    OTRA_MAQUINARIA_Y_EQUIPO = 'I08'
    POR_DEFINIR = 'P01'
    SIN_EFECTOS_FISCALES = 'S01'


class Exportacion(StrEnum):
    NO_APLICA = '01'
    DEFINITIVA_CON_CLAVE_A1 = '02'
    TEMPORAL = '03'
    DEFINITIVA_CON_CLAVE_DISTINTA_A_A1_O_CUANDO_NO_EXISTE_ENAJENACION_EN_TERMINOS_DEL_CFF = '04'


class ObjetoImp(StrEnum):
    NO_OBJETO_DE_IMPUESTO = '01'
    SI_OBJETO_DE_IMPUESTO = '02'
    SI_OBJETO_DEL_IMPUESTO_Y_NO_OBLIGADO_AL_DESGLOSE = '03'
    SI_OBJETO_DEL_IMPUESTO_Y_NO_CAUSA_IMPUESTO = '04'
    SI_OBJETO_DEL_IMPUESTO_IVA_CREDITO_PODEBI = '05'


class Banco(StrEnum):
    BANAMEX = '002'
    BANCOMEXT = '006'
    BANOBRAS = '009'
    BBVA_BANCOMER = '012'
    SANTANDER = '014'
    BANJERCITO = '019'
    HSBC = '021'
    BAJIO = '030'
    IXE = '032'
    INBURSA = '036'
    INTERACCIONES = '037'
    MIFEL = '042'
    SCOTIABANK = '044'
    BANREGIO = '058'
    INVEX = '059'
    BANSI = '060'
    AFIRME = '062'
    BANORTE = '072'
    THE_ROYAL_BANK = '102'
    AMERICAN_EXPRESS = '103'
    BAMSA = '106'
    TOKYO = '108'
    JP_MORGAN = '110'
    BMONEX = '112'
    VE_POR_MAS = '113'
    ING = '116'
    DEUTSCHE = '124'
    CREDIT_SUISSE = '126'
    AZTECA = '127'
    AUTOFIN = '128'
    BARCLAYS = '129'
    COMPARTAMOS = '130'
    BANCO_FAMSA = '131'
    BMULTIVA = '132'
    ACTINVER = '133'
    WAL_MART = '134'
    NAFIN = '135'
    INTERBANCO = '136'
    BANCOPPEL = '137'
    ABC_CAPITAL = '138'
    UBS_BANK = '139'
    CONSUBANCO = '140'
    VOLKSWAGEN = '141'
    CIBANCO = '143'
    BBASE = '145'
    BANKAOOL = '147'
    PAGATODO = '148'
    FORJADORES = '149'
    INMOBILIARIO = '150'
    DONDE = '151'
    BANCREA = '152'
    PROGRESO = '153'
    BANCO_FINTERRA = '154'
    ICBC = '155'
    SABADELL = '156'
    SHINHAN = '157'
    MIZUHO_BANK = '158'
    BANK_OF_CHINA = '159'
    BANCO_S3 = '160'
    BANSEFI = '166'
    HIPOTECARIA_FEDERAL = '168'
    MONEXCB = '600'
    GBM = '601'
    MASARI = '602'
    VALUE = '605'
    ESTRUCTURADORES = '606'
    TIBER = '607'
    VECTOR = '608'
    BYB = '610'
    ACCIVAL = '614'
    MERRILL_LYNCH = '615'
    FINAMEX = '616'
    VALMEX = '617'
    UNICA = '618'
    MAPFRE = '619'
    PROFUTURO = '620'
    CB_ACTINVER = '621'
    OACTIN = '622'
    SKANDIA_VIDA = '623'
    CBDEUTSCHE = '626'
    ZURICH = '627'
    ZURICHVI = '628'
    SU_CASITA = '629'
    CB_INTERCAM = '630'
    CI_BOLSA = '631'
    BULLTICK_CB = '632'
    STERLING = '633'
    FINCOMUN = '634'
    HDI_SEGUROS = '636'
    ORDER = '637'
    AKALA = '638'
    CB_JPMORGAN = '640'
    REFORMA = '642'
    STP = '646'
    TELECOMM = '647'
    EVERCORE = '648'
    SKANDIA_OPERADORA_DE_FONDOS = '649'
    SEGMTY = '651'
    ASEA = '652'
    KUSPIT = '653'
    SOFIEXPRESS = '655'
    UNAGRA = '656'
    OPCIONES_EMPRESARIALES_DEL_NOROESTE = '659'
    LIBERTAD = '670'
    CLS = '901'
    INDEVAL = '902'
    NA = '999'


