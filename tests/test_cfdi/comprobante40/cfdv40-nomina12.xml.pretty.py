{'Certificado': '',
 'CfdiRelacionados': [{'CfdiRelacionado': ['F4F09AEF-57F2-4BE0-A828-87D1A80ED61C'],
                       'TipoRelacion': Code('09', 'Factura generada por pagos diferidos')}],
 'Complemento': {'Nomina': {'Deducciones': {'Deduccion': [{'Clave': 'XXX',
                                                           'Concepto': 'Deduccion '
                                                                       'Semanal',
                                                           'Importe': Decimal('10.00'),
                                                           'TipoDeduccion': Code('001', 'Seguridad social')},
                                                          {'Clave': 'YYY',
                                                           'Concepto': 'Deduccion '
                                                                       'Semanal',
                                                           'Importe': Decimal('10.00'),
                                                           'TipoDeduccion': Code('100', 'Ajuste en Viáticos exentos')}],
                                            'TotalImpuestosRetenidos': Decimal('123.45'),
                                            'TotalOtrasDeducciones': Decimal('123.45')},
                            'Emisor': {'Curp': 'OAAJ840102HJCVRN00',
                                       'EntidadSNCF': {'MontoRecursoPropio': Decimal('123.45'),
                                                       'OrigenRecurso': Code('IP', 'Ingresos propios')},
                                       'RegistroPatronal': 'E23-12345-12-1',
                                       'RfcPatronOrigen': 'AAA010101AAA'},
                            'FechaFinalPago': datetime.date(2016, 10, 15),
                            'FechaInicialPago': datetime.date(2016, 10, 1),
                            'FechaPago': datetime.date(2016, 10, 15),
                            'Incapacidades': [{'DiasIncapacidad': 1,
                                               'ImporteMonetario': Decimal('22.45'),
                                               'TipoIncapacidad': Code('01', 'Riesgo de trabajo')},
                                              {'DiasIncapacidad': 2,
                                               'ImporteMonetario': Decimal('22.45'),
                                               'TipoIncapacidad': Code('02', 'Enfermedad en general')}],
                            'NumDiasPagados': Decimal('15'),
                            'OtrosPagos': [{'Clave': '003',
                                            'CompensacionSaldosAFavor': {'Año': 2016,
                                                                         'RemanenteSalFav': Decimal('1234.56'),
                                                                         'SaldoAFavor': Decimal('12345.67')},
                                            'Concepto': 'Otro pago 111',
                                            'Importe': Decimal('1234.56'),
                                            'SubsidioAlEmpleo': Decimal('1234.56'),
                                            'TipoOtroPago': Code('001', 'Reintegro de ISR pagado en exceso (siempre que no haya sido enterado al SAT)')},
                                           {'Clave': '003',
                                            'CompensacionSaldosAFavor': {'Año': 2016,
                                                                         'RemanenteSalFav': Decimal('123.45'),
                                                                         'SaldoAFavor': Decimal('123.45')},
                                            'Concepto': 'Otro pago 222',
                                            'Importe': Decimal('1234.56'),
                                            'SubsidioAlEmpleo': Decimal('1234.56'),
                                            'TipoOtroPago': Code('002', 'Subsidio para el empleo (efectivamente entregado al trabajador)')}],
                            'Percepciones': {'JubilacionPensionRetiro': {'IngresoAcumulable': Decimal('223.45'),
                                                                         'IngresoNoAcumulable': Decimal('223.45'),
                                                                         'MontoDiario': Decimal('223.45'),
                                                                         'TotalParcialidad': Decimal('223.45'),
                                                                         'TotalUnaExhibicion': Decimal('223.45')},
                                             'Percepcion': [{'AccionesOTitulos': {'PrecioAlOtorgarse': Decimal('123.45'),
                                                                                  'ValorMercado': Decimal('12345.67')},
                                                             'Clave': 'AAA',
                                                             'Concepto': 'Sueldo '
                                                                         'Regular',
                                                             'HorasExtra': [{'Dias': 2,
                                                                             'HorasExtra': 8,
                                                                             'ImportePagado': Decimal('228.45'),
                                                                             'TipoHoras': Code('01', 'Dobles')},
                                                                            {'Dias': 2,
                                                                             'HorasExtra': 8,
                                                                             'ImportePagado': Decimal('228.45'),
                                                                             'TipoHoras': Code('02', 'Triples')}],
                                                             'ImporteExento': Decimal('90.00'),
                                                             'ImporteGravado': Decimal('89.00'),
                                                             'TipoPercepcion': Code('001', 'Sueldos, Salarios Rayas y Jornales')},
                                                            {'Clave': 'BBB',
                                                             'Concepto': 'Sueldo '
                                                                         'Regular',
                                                             'HorasExtra': [{'Dias': 2,
                                                                             'HorasExtra': 8,
                                                                             'ImportePagado': Decimal('288.45'),
                                                                             'TipoHoras': Code('01', 'Dobles')},
                                                                            {'Dias': 2,
                                                                             'HorasExtra': 8,
                                                                             'ImportePagado': Decimal('288.45'),
                                                                             'TipoHoras': Code('03', 'Simples')}],
                                                             'ImporteExento': Decimal('90.00'),
                                                             'ImporteGravado': Decimal('89.00'),
                                                             'TipoPercepcion': Code('005', 'Fondo de Ahorro')}],
                                             'SeparacionIndemnizacion': {'IngresoAcumulable': Decimal('323.45'),
                                                                         'IngresoNoAcumulable': Decimal('323.45'),
                                                                         'NumAñosServicio': 7,
                                                                         'TotalPagado': Decimal('323.45'),
                                                                         'UltimoSueldoMensOrd': Decimal('323.45')},
                                             'TotalExento': Decimal('123.45'),
                                             'TotalGravado': Decimal('123.45'),
                                             'TotalJubilacionPensionRetiro': Decimal('123.45'),
                                             'TotalSeparacionIndemnizacion': Decimal('123.45'),
                                             'TotalSueldos': Decimal('123.45')},
                            'Receptor': {'Antigüedad': 'P3Y2M23D',
                                         'Banco': Code('002', 'BANAMEX'),
                                         'ClaveEntFed': Code('AGU', 'Aguascalientes'),
                                         'CuentaBancaria': 1234567890,
                                         'Curp': 'OAAJ840102HJCVRN00',
                                         'Departamento': '001',
                                         'FechaInicioRelLaboral': datetime.date(2013, 4, 11),
                                         'NumEmpleado': '001',
                                         'NumSeguridadSocial': '123456789012345',
                                         'PeriodicidadPago': Code('04', 'Quincenal'),
                                         'Puesto': 'Programador',
                                         'RiesgoPuesto': Code('3', 'Clase III'),
                                         'SalarioBaseCotApor': Decimal('123.45'),
                                         'SalarioDiarioIntegrado': Decimal('123.45'),
                                         'Sindicalizado': 'Sí',
                                         'SubContratacion': [{'PorcentajeTiempo': Decimal('23.45'),
                                                              'RfcLabora': 'AAA010101AAA'},
                                                             {'PorcentajeTiempo': Decimal('13.45'),
                                                              'RfcLabora': 'BBB010101AAA'}],
                                         'TipoContrato': Code('01', 'Contrato de trabajo por tiempo indeterminado'),
                                         'TipoJornada': Code('02', 'Nocturna'),
                                         'TipoRegimen': Code('03', 'Jubilados')},
                            'TipoNomina': Code('O', 'Nómina ordinaria'),
                            'TotalDeducciones': Decimal('123.45'),
                            'TotalOtrosPagos': Decimal('123.45'),
                            'TotalPercepciones': Decimal('123.45'),
                            'Version': '1.2'}},
 'Conceptos': [{'Cantidad': Decimal('1'),
                'ClaveProdServ': Code('84111506', 'Servicios de facturación'),
                'ClaveUnidad': Code('ACT', 'Actividad'),
                'Descripcion': 'Descripcion',
                'Importe': Decimal('0'),
                'ObjetoImp': Code('01', 'No objeto de impuesto'),
                'ValorUnitario': Decimal('0')}],
 'Emisor': {'Nombre': 'Esta es una demostración',
            'RegimenFiscal': Code('622', 'Actividades Agrícolas, Ganaderas, Silvícolas y Pesqueras'),
            'Rfc': ' AAA010101AAA'},
 'Exportacion': Code('03', 'Temporal'),
 'Fecha': datetime.datetime(2021, 12, 8, 23, 59, 59),
 'FormaPago': Code('02', 'Cheque nominativo'),
 'LugarExpedicion': '99999',
 'Moneda': Code('XXX', 'Los códigos asignados para las transacciones en que intervenga ninguna moneda'),
 'NoCertificado': '30001000000300023708',
 'Receptor': {'DomicilioFiscalReceptor': '99999',
              'Nombre': 'Juanito Bananas De la Sierra',
              'RegimenFiscalReceptor': Code('630', 'Enajenación de acciones en bolsa de valores'),
              'Rfc': 'BASJ600902KL9',
              'UsoCFDI': Code('P01', 'Por definir')},
 'Sello': '',
 'SubTotal': Decimal('0'),
 'TipoDeComprobante': Code('P', 'Pago'),
 'Total': Decimal('0'),
 'Version': '4.0'}