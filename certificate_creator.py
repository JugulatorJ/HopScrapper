from certificates import HopsteinerHopCertificate, HolingberyHopCertificate, CrosbyHopCertificate, GlacierHopCertificate


class CertGenerator:
    def __init__(self, producer):
        self.producer = producer

    def generate_hop_cert_dict(self, soup_source, entry_id):

        if self.producer == 'hopsteiner':

            lot_id = HopsteinerHopCertificate(soup_source).get_lot_id()
            contract_number = HopsteinerHopCertificate(soup_source).get_contract_number()
            hop_name = HopsteinerHopCertificate(soup_source).get_hop_name()
            crop_year = HopsteinerHopCertificate(soup_source).get_crop_year()
            alpha_acid = HopsteinerHopCertificate(soup_source).get_alpha_acid()
            beta_acid = HopsteinerHopCertificate(soup_source).get_beta_acid()
            total_oil = HopsteinerHopCertificate(soup_source).get_total_oil()
            cohumulone = HopsteinerHopCertificate(soup_source).get_cohumulone()
            hop_cert_dict = {'entry_id': entry_id, 'lot_id': lot_id, 'contract_number': contract_number,
                             'hop_name': hop_name, 'crop_year': crop_year, 'alpha_acid': alpha_acid,
                             'beta_acid': beta_acid, 'total_oil': total_oil, 'cohumulone': cohumulone}
            return hop_cert_dict

        elif self.producer == 'hollingbery':
            lot_id = HolingberyHopCertificate(soup_source).get_lot_id()
            contract_number = HolingberyHopCertificate(soup_source).get_contract_number()
            hop_name = HolingberyHopCertificate(soup_source).get_hop_name()
            crop_year = HolingberyHopCertificate(soup_source).get_crop_year()
            alpha_acid = HolingberyHopCertificate(soup_source).get_alpha_acid()
            beta_acid = HolingberyHopCertificate(soup_source).get_beta_acid()
            total_oil = HolingberyHopCertificate(soup_source).get_total_oil()
            cohumulone = HolingberyHopCertificate(soup_source).get_cohumulone()
            hop_cert_dict = {'entry_id': entry_id, 'lot_id': lot_id, 'contract_number': contract_number,
                             'hop_name': hop_name, 'crop_year': crop_year, 'alpha_acid': alpha_acid,
                             'beta_acid': beta_acid, 'total_oil': total_oil, 'cohumulone': cohumulone}

            print(hop_cert_dict)
            print('\n')
            return hop_cert_dict

        elif self.producer == 'crosbyhops':
            lot_id = CrosbyHopCertificate(soup_source).get_lot_id()
            contract_number = CrosbyHopCertificate(soup_source).get_contract_number()
            hop_name = CrosbyHopCertificate(soup_source).get_hop_name()
            crop_year = CrosbyHopCertificate(soup_source).get_crop_year()
            alpha_acid = CrosbyHopCertificate(soup_source).get_alpha_acid()
            beta_acid = CrosbyHopCertificate(soup_source).get_beta_acid()
            total_oil = CrosbyHopCertificate(soup_source).get_total_oil()
            cohumulone = CrosbyHopCertificate(soup_source).get_cohumulone()
            hop_cert_dict = {'entry_id': entry_id, 'lot_id': lot_id, 'contract_number': contract_number,
                             'hop_name': hop_name, 'crop_year': crop_year, 'alpha_acid': alpha_acid,
                             'beta_acid': beta_acid, 'total_oil': total_oil, 'cohumulone': cohumulone}
            print(hop_cert_dict)
            print('\n')
            return hop_cert_dict

        elif self.producer == 'glacierhops':
            lot_id = GlacierHopCertificate(soup_source).get_lot_id()
            contract_number = GlacierHopCertificate(soup_source).get_contract_number()
            hop_name = GlacierHopCertificate(soup_source).get_hop_name()
            crop_year = GlacierHopCertificate(soup_source).get_crop_year()
            alpha_acid = GlacierHopCertificate(soup_source).get_alpha_acid()
            beta_acid = GlacierHopCertificate(soup_source).get_beta_acid()
            total_oil = GlacierHopCertificate(soup_source).get_total_oil()
            cohumulone = GlacierHopCertificate(soup_source).get_cohumulone()
            hop_cert_dict = {'entry_id': entry_id, 'lot_id': lot_id, 'contract_number': contract_number,
                             'hop_name': hop_name, 'crop_year': crop_year, 'alpha_acid': alpha_acid,
                             'beta_acid': beta_acid, 'total_oil': total_oil, 'cohumulone': cohumulone}
            print(hop_cert_dict)
            print('\n')
            return hop_cert_dict

    @staticmethod
    def generate_scrap_denied(entry_id):
        hop_cert_dict = {'entry_id': entry_id, 'lot_id': None, 'contract_number': None,
                         'hop_name': None, 'crop_year': None, 'alpha_acid': None,
                         'beta_acid': None, 'total_oil': None, 'cohumulone': None}
        print(hop_cert_dict)
        return hop_cert_dict
