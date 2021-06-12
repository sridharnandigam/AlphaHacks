//
//  CompanyDetailsView.swift
//  AlphaHacks
//
//  Created by Arpan Dhatt on 6/12/21.
//

import SwiftUI

struct CompanyDetailsView: View {
    @EnvironmentObject var appState: AppState
    var company: String
    var body: some View {
        ScrollView {
            CompanyCard().padding()
        }.navigationTitle(appState.selectedCompany)
    }
}

struct CompanyDetailsView_Previews: PreviewProvider {
    static var previews: some View {
        CompanyDetailsView(company: "Test Company").environmentObject(AppState())
    }
}
