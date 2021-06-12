//
//  CompanyCard.swift
//  AlphaHacks
//
//  Created by Arpan Dhatt on 6/12/21.
//

import SwiftUI

struct CompanyCard: View {
    @EnvironmentObject var appState: AppState
    
    var body: some View {
        VStack(alignment: .leading) {
            Text("Sustainability Rating: " + String(appState.company_details.rating)).font(.subheadline)
            Divider()
            Text(appState.company_details.description).font(.caption).padding()
            VStack(alignment: .leading) {
                ForEach(appState.company_details.articles, id: \.link) {article in
                    ArticleCard(article: article)
                }
            }.padding()
        }
    }
}

struct CompanyCard_Previews: PreviewProvider {
    static var previews: some View {
        CompanyCard().environmentObject(AppState())
    }
}
